import socket
import json
import sys

class pyServ():

    def __init__(self, TCP_IP="127.0.0.1", TCP_PORT=9000, Listen=4,buff=1024):
        self.addr = (TCP_IP, TCP_PORT)
        self.bufferSize = buff
        self.listen = Listen
        self.function = {}
        self.packetConn = None
        self.socketConn = None
        self.DefaultResponse = "I am a Default Response"

    def __executeFunc__(self, funcName, args):
        try:
            response = self.function[funcName](*args)
            return response
        except Exception as e:
            return e

    def connect(self):
        self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketConn.bind(self.addr)
        self.socketConn.listen(self.listen)
        try:
            self.packetConn, client_address = self.socketConn.accept()
        except KeyboardInterrupt:
            print "Receive Signal Interrupt"
            self.packetConn.close()

    def getRPC(self):
        rpc = self.payload()
        functionName = rpc["method"]
        if functionName in self.function:
            arguments = rpc["args"]
            resp = self.__executeFunc__(functionName, arguments)
            print resp
            self.sendResponse(resp)
            return True
        self.sendResponse("Function not Registered at Server Side")
        return False

    def payload(self):
        data = self.packetConn.recv(self.bufferSize)
        try:
            jsonData = json.dumps(data)
            jsonData = json.loads(data)
            return jsonData
        except Exception as e:
            return e

    def register_function(self,func):
        try:
            self.function[func.func_name] = func
            return True
        except:
            return False

    def receive(self):
        return self.payload()

    def RPCServer(self):
        try:
            while True:
                try:
                    connection, client_address = self.socketConn.accept()
                    self.packetConn = connection
                except KeyboardInterrupt as e:
                        print "Signal Interrupt..."
                        self.sendResponse(e)
                        connection.close()
                rpc = self.payload()
                functionName = rpc["method"]
                if functionName in self.function:
                    arguments = rpc["args"]
                    resp = self.__executeFunc__(functionName, arguments)
                    self.sendResponse(resp)
                    self.sendResponse("Function not Registered at Server Side")
        except Exception as e:
                print e


    def sendDefaultResponse(self):
        self.packetConn.send(json.dumps({"response":self.DefaultResponse}, encoding='utf-8'))

    def sendResponse(self,respData):
        resp = json.dumps({"response":str(respData)}, encoding='utf-8')
        self.packetConn.send(resp)

    def serve_forever(self):
        print "TCP Server Listening on ",self.addr
        while True:
            connection, client_address = self.socketConn.accept()
            self.packetConn = connection
            data = self.payload()
            print data

    def setDefaultResponse(self, defResponse):
        self.setDefaultResponse = defResponse

    def unregister_function(self, func):
        try:
            del self.function[func.func_name]
            return True
        except Exception as e:
            return False
