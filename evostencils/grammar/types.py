class Types:
    @staticmethod
    def _init_type(identifier, types, type_attribute=None, guard=False):
        if type_attribute is None:
            type_attribute = identifier
        if types is None:
            return Type(identifier, guard)
        else:
            return getattr(types, type_attribute)

    def __init__(self, level, previous_types=None):
        # Fine-grid types
        gen_id = lambda base: f"{base}_{2**level}h"
        self.S_h = self._init_type(gen_id("S"), previous_types, "S_2h")
        self.S_guard_h = self._init_type(gen_id("S_guard"), previous_types, "S_guard_2h", guard=True)
        self.C_h = self._init_type(gen_id("C"), previous_types, "C_2h")
        self.C_guard_h = self._init_type(gen_id("C_guard"), previous_types, "C_guard_2h", guard=True)
        self.x_h = self._init_type(gen_id("x"), previous_types, "x_2h")
        self.A_h = self._init_type(gen_id("A"), previous_types, "A_2h")
        self.B_h = self._init_type(gen_id("A"), previous_types, "B_2h")
        self.R_h = Type(f"R_{2**level}h")

        # Coarse-grid types
        gen_id = lambda base: f"{base}_{2**level+1}h"
        self.S_2h = Type(gen_id("S"))
        self.S_guard_2h = Type(gen_id("S_guard"), guard=True)
        self.C_2h = Type(gen_id("C"))
        self.C_guard_2h = Type(gen_id("C_guard"), guard=True)
        self.x_2h = Type(gen_id("x"))
        self.A_2h = Type(gen_id("A"))
        self.B_2h = Type(gen_id("B"))
        self.P_2h = Type(gen_id("P"))
        self.CGS_2h = Type(gen_id("CGC"))

        # General types
        self.Partitioning = self._init_type("Partitioning", previous_types)
        self.RelaxationFactorIndex = self._init_type("RelaxationFactorIndex", previous_types)
