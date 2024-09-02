class BAG:
    def __init__(self,Eraser,pencil,pen,sharpner,):
        self.Eraser=Eraser#public variable
        self._pencil=pencil#protected variable
        self.__pen=pen#private variable
        self.sharpner=sharpner#public variable
        self._items=['Eraser','pencil','sharpner']
    def Things_inside_Bag(self):#public method
        for i in self._items:
            print(i)
    def _addThings(self,pen):#protected method
        self._items.append(pen)
        print(self._items)

    def __remove(self,obj):#private method
        if obj in self._items :
            self._items.remove(obj)
        print(self._items)
b1=BAG('apsara_eraser','apsra_pencil','cellopen','apsara_sharpner')
b1.Things_inside_Bag()#public method called
b1._addThings('Ronalds')#protected method called
b1._BAG__remove('sharpner')#private method called