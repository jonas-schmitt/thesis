from deap import gp

class PrimitiveSetTyped(gp.PrimitiveSetTyped):
    def _add(self, prim):
        def addType(dict_, ret_type):
            if ret_type not in dict_:
                new_list = []
                for type_, list_ in dict_.items():
                    # Use __equal__ instead of issubclass
                    if ret_type == type_:
                        for item in list_:
                            if item not in new_list:
                                new_list.append(item)
                dict_[ret_type] = new_list

        addType(self.primitives, prim.ret)
        addType(self.terminals, prim.ret)

        self.mapping[prim.name] = prim
        if isinstance(prim, gp.Primitive):
            for type_ in prim.args:
                addType(self.primitives, type_)
                addType(self.terminals, type_)
            dict_ = self.primitives
        else:
            dict_ = self.terminals

        for type_ in dict_:
            if type_ == prim.ret:
                dict_[type_].append(prim)

