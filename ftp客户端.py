import socket,os,json,struct,sys,hashlib,time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip1 = '192.168.241.135'
ip2 = '127.0.0.1'
phone.connect(('{}'.format(ip1),8080))

while 1:
    try:
        username = input('用户名>>:')
        m=hashlib.md5('bailu'.encode('utf-8'))
        m.update(username.encode('utf-8'))
        username=m.hexdigest()

        if username:
            username2 = bytes(username, encoding='utf-8')

        else:
            continue

        password = input('密码>>:')
        m = hashlib.md5('bailu'.encode('utf-8'))
        m.update(password.encode('utf-8'))
        password = m.hexdigest()
        if password:
            password2 = bytes(password, encoding='utf-8')
            phone.send(username2)
            time.sleep(1)
            phone.send(password2)
        else:
            continue
        reply=phone.recv(1024)
        reply2=reply.decode('utf-8')
        print(reply2)  #是否成功

        if reply2=='登录失败':
            continue
        else:
            pass

        reply3 = phone.recv(100)
        reply4 = reply3.decode('utf-8')
        print(reply4)           #文件目录
        time.sleep(0.3)
        reply5 = phone.recv(1024)
        reply6 = reply5.decode('utf-8')
        print(reply6)            #文件内容

        func=input('您需要： 1.上传文件'
                   '        2.下载文件\n')
        func2=bytes(func,encoding='utf-8')
        phone.send(func2)

        if func=='1':
            path=input('文件路径：')
            if os.path.isfile(path):
                data='1'
                data2=bytes(data,encoding='utf-8')
                time.sleep(2)
                phone.send(data2)
                time.sleep(2)
            else:
                data = '2'
                data2 = bytes(data, encoding='utf-8')
                phone.send(data2)
                print('文件不存在！')
                continue

            filename=os.path.basename(path)
            size=os.path.getsize(path)
            dic        ={'path':path,'filename':filename,'size':size}
            json_dic   =json.dumps(dic)
            json_dic_b =bytes(json_dic,encoding='utf-8')
            head_len   =struct.pack('i',len(json_dic_b))
            phone.send(head_len)
            phone.send(json_dic_b)

            zone = phone.recv(1024).decode('utf-8')
            if zone == '1':
                print('空间不足！')
                select=input('是否充钱加100M (Y/N) ?\n')
                if select=='Y':
                    data='1'
                    data2=bytes(data,encoding='utf-8')
                    phone.send(data2)
                else:
                    data = '2'
                    data2 = bytes(data, encoding='utf-8')
                    phone.send(data2)

                    continue
            else:
                pass


            send_size=0
            with open(path,'rb') as f:
                for line in f:
                    m=hashlib.md5('bailu'.encode('utf-8'))
                    m.update(line)
                    phone.send(line)
                    send_size += len(line)

                    width = 70
                    percent = send_size / size

                    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
                    print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')

            print('\n')

        elif func == '2':
            filename=input('下载文件：')
            filename2=bytes(filename,encoding='utf-8')
            phone.send(filename2)

            data=phone.recv(1024).decode('utf-8')

            if data=='2':

                data1 = phone.recv(4)
                data2 = struct.unpack('i', data1)[0]

                head = phone.recv(data2)
                head2 = head.decode('utf-8')
                head3 = json.loads(head2)

                filepath=input('下载路径：')

                sized = 0

                file=os.path.join(filepath,filename)
                with open(file, 'wb') as f:
                    while sized < head3['size']:
                        data = phone.recv(8192)

                        f.write(data)
                        sized += len(data)

                        width=70
                        percent=sized/head3['size']
                        show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
                        print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')
                    print('\n')
            else:
                print('文件不存在！')
                continue
        else:
            print('请输入1或2！')
            continue
        print('success\n')
    except:
        break
