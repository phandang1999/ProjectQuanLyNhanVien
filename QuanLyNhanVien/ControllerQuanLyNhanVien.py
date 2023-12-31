from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *

class ControllerNhanVien:
    def __init__(self, model: ModuleNhanVien, view: ViewQuanLyNhanVien):
        self.model = model
        self.view = view
        self.loaiNV = ''

        self.view.btnLoadNV.config(command=self.loadNV)
        self.view.btnTimKiem.config(command=self.timNV)
        self.view.btnThemNV.config(command=self.themNV)
        self.view.btnXoaNV.config(command=self.xoaNV)
        self.view.btnCapnhatNV.config(command=self.capnhatNV)
        self.view.btntinhLuongNV.config(command=self.tinhluongNV)
    def loadNV(self):
        self.model.setdsNVnull()
        self.view.clearTreeview()
        self.model.loadNV()
        self.view.showNV(self.model.dsNV)
        #Test hiển thị
        # for nv in self.model.dsNV:
        #     print("Test", nv)
    def timNV(self):
        self.model.setdsNVnull()
        self.model.timNV(self.view.maNVCanTim.get())
        self.view.clearTreeview()
        self.view.showNV(self.model.dsNV)
        if self.model.dsNV == []: self.view.messageWR("Tìm không có sinh viên")

    def themNV(self):
        self.model.setdsNVnull()
        thucThi = 0
        if self.view.loaiNV.get() != 'Chọn nhân viên':
            self.loaiNV = self.view.loaiNV.get()

        dataNV = [self.view.maNV.get(), self.view.hoTen.get(), self.view.luongCB.get(), self.loaiNV,
                self.view.soNgayLam.get(), self.view.soSanPham.get()]

        self.model.timNV(self.view.maNV.get())

        for i in dataNV:
            if i == '':
                thucThi = 1

        if (thucThi == 0) & (self.model.dsNV == []):
            self.model.themNV(dataNV)
            self.view.clearTreeview()
            self.model.loadNV()
            self.view.showNV(self.model.dsNV)
            print("Them thanh cong nhan vien")
        else:
            print("Them khong thanh cong nhan vien")
            self.view.messageWR("Thêm không thành công nhân viên")
    def xoaNV(self):
        self.model.setdsNVnull()
        self.model.xoaNV(self.view.ojSelected)
        self.view.clearTreeview()
        self.model.loadNV()
        self.view.showNV(self.model.dsNV)
        print("Xoa thanh cong nhan vien")

    def capnhatNV(self):
        self.model.setdsNVnull()
        thucThi = 0

        if self.view.loaiNV.get() != 'Chọn nhân viên':
            self.loaiNV = self.view.loaiNV.get()

        dataNV = [self.view.maNV.get(), self.view.hoTen.get(), self.view.luongCB.get(), self.loaiNV,
                  self.view.soNgayLam.get(), self.view.soSanPham.get()]

        for i in dataNV:
            if i == '':
                thucThi = 1

        if thucThi == 0:
            self.model.capnhatNV(dataNV)
            self.view.clearTreeview()
            self.model.loadNV()
            self.view.showNV(self.model.dsNV)

        if (self.view.maNV.get() != self.view.ojSelected[0]) | (thucThi == 1):
            self.view.messageWR("Cập nhật không thành công nhân viên")

    def tinhluongNV(self):
        self.model.setdsNVnull()
        datatinhluongNV = [self.view.maNV.get(), self.view.hoTen.get(), self.view.loaiNV.get(), self.view.luongCB.get(),
                           int(self.view.soNgayLam.get()), int(self.view.soSanPham.get()), self.view.htluongHT.get()]
        if datatinhluongNV == self.view.ojSelected:
            if datatinhluongNV[2] == 'Văn Phòng':
                luongHT = float(datatinhluongNV[3]) + datatinhluongNV[5] * 150000
            elif datatinhluongNV[2] == 'Bán Hàng':
                luongHT = float(datatinhluongNV[3]) + datatinhluongNV[5] * 100000
            else: luongHT = float(datatinhluongNV[3]) + datatinhluongNV[5] * 50000
            self.model.tinhluongHT(datatinhluongNV,luongHT)
            self.view.clearTreeview()
            self.model.loadNV()
            self.view.showNV(self.model.dsNV)
        else:
            self.view.messageWR("Vui lòng chọn lại nhân viên cần tính lương")
