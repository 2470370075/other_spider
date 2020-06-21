import socket,os,json,struct,socketserver,time,hashlib

info={'wjx':'123','wjx2':'234','wjx3':'345'}
path={'wjx':'upload1','wjx2':'upload2','wjx3':'upload3'}
size={'wjx':104857600,'wjx2':104857600,'wjx3':104857600}

# 继承此类应该是为了实现多个客户端
class mylink(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            time.sleep(1)
            username = self.request.recv(1024).decode('utf-8')
            password = self.request.recv(1024).decode('utf-8')

            for i in info:

                m = hashlib.md5('bailu'.encode('utf-8'))
                m.update(i.encode('utf-8'))

                if username==m.hexdigest():
                    username=i
                    print(username)

            n = hashlib.md5('bailu'.encode('utf-8'))
            n.update(info[username].encode('utf-8'))

            if username in info and password == n.hexdigest():
                reply = '登录成功'


            else:
                reply = '登录失败'
                reply2 = bytes(reply, encoding='utf-8')
                self.request.send(reply2)

                continue
            reply2 = bytes(reply, encoding='utf-8')
            self.request.send(reply2)

            userpath='您的家在：%s'%(path[username])
            userpath2=bytes(userpath,encoding='utf-8')
            self.request.send(userpath2)
            time.sleep(0.1)

            dir=os.listdir(path[username])
            dir='里面的文件为：%s'%(dir)
            dir=str(dir)
            dir1=bytes(dir,encoding='utf-8')

            self.request.send(dir1)


            func=self.request.recv(1024).decode('utf-8')
            print(func)
            if func=='1':

                data=self.request.recv(1024).decode('utf-8')
                print('daya://///',data)
                if data=='1':
                    pass
                else:
                    continue

                data1=self.request.recv(4)
                data2=struct.unpack('i',data1)[0]
                print(data2)

                head = self.request.recv(data2)
                head2=head.decode('utf-8')
                head3=json.loads(head2)
                print(head3)

                dir = os.listdir(path[username])
                innersize=0
                for i in dir :
                    innersize+=os.path.getsize(i)
                if innersize+head3['size']>size[username]:
                    print('空间不足！')
                    data='1'
                    data2=bytes(data,encoding='utf-8')
                    self.request.send(data2)


                    select = self.request.recv(1024).decode('utf-8')
                    if select == '1':
                        size[username]+=104857600
                    else:
                        continue
                else:
                    data = '2'
                    data2 = bytes(data.encode('utf-8'))
                    self.request.send(data2)

                file=os.path.join(path[username],head3['filename'])
                sized=0
                print(file)
                with open(file,'wb') as f:
                    while sized<head3['size']:
                        n=hashlib.md5('bailu'.encode('utf-8'))

                        data=self.request.recv(8192)
                        n.update(data)

                        f.write(data)
                        sized+=len(data)
                        print(len(data))
                data=self.request.recv(8192)
                if n.hexdigest()==data.decode('utf-8'):
                    print('文件完整！')
                else:
                    print('文件不完整！')

            elif func == '2':
                filename2=self.request.recv(1024).decode('utf-8')
                print(filename2)
                data3 = '0'
                for i in os.listdir(path[username]):

                    if i==filename2:
                        data3 = '2'
                        data2 = bytes(data3, encoding='utf-8')

                        self.request.send(data2)

                        filepath2=os.path.join(path[username],filename2)
                        size2=os.path.getsize(filepath2)
                        dic2={'path':filepath2,'filename':filename2,'size':size2}

                        json_dic = json.dumps(dic2)
                        json_dic_b = bytes(json_dic, encoding='utf-8')
                        head_len = struct.pack('i', len(json_dic_b))

                        self.request.send(head_len)
                        self.request.send(json_dic_b)

                        with open(filepath2, 'rb') as f:
                            data = f.read()
                            self.request.send(data)
                if data3 != '2':
                    data3='1'
                    data2=bytes(data3,encoding='utf-8')
                    self.request.send(data2)
                    continue
            else:
                continue
            print('success')
ip1 = '192.168.241.135'
ip2 = '127.0.0.1'
server=socketserver.ThreadingTCPServer(('{}'.format(ip1),8080),mylink)
server.serve_forever()














