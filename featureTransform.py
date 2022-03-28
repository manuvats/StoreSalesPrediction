from datetime import date


class featureTransform:

    def __init__(self, item_id, ifat_content, oestd_yr, osize, oloc, otype):

        try:
            self.item_id = item_id
            self.ifat_content = ifat_content
            self.oestd_yr = oestd_yr
            self.osize = osize
            self.oloc = oloc
            self.otype = otype
        except Exception as e:
            raise Exception(f"(__init__): Something went wrong on initiation process\n" + str(e))

    def itemType(self):
        try:
            category = self.item_id[0:2]
            #item_expanded = {'FD': 'Food',
                             #'NC': 'Non-Consumable',
                             # 'DR': 'Drinks'}
            #for key in item_expanded.keys():
                #category = temp.upper().replace(key, item_expanded[key])
            food = drinks = noncons = 0
            if category == 'FD':
                food = 1
            elif category == 'NC':
                noncons = 1
            else:
                drinks = 1
            return {'food': food, 'noncons': noncons, 'drinks': drinks}
        except Exception as e:
            raise Exception(f"(itemID): Something went wrong in transforming itemID\n" + str(e))

    def fatContent(self):
        try:
            lowfat = regular = nonedible = 0
            if self.ifat_content == 'low_fat':
                lowfat = 1
            elif self.ifat_content == 'regular':
                regular = 1
            else:
                nonedible = 1
            return {'lowfat': lowfat, 'regular': regular, 'nonedible': nonedible}
        except Exception as e:
            raise Exception(f"(fatContent): Something went wrong in transforming fat content\n" + str(e))

    def outletYrs(self):
        try:
            outlet_yrs = date.today().year - self.oestd_yr
            return outlet_yrs
        except Exception as e:
            raise Exception(f"(outletYrs): Something went wrong in transforming Outlet Established Year\n" + str(e))

    def outletSize(self):
        try:
            small = medium = high = 0
            if self.osize == 'small':
                small = 1
            elif self.osize == 'medium':
                medium = 1
            else:
                high = 1
            return {'small': small, 'medium': medium, 'high': high}
        except Exception as e:
            raise Exception(f"(outletYrs): Something went wrong in transforming Outlet Size\n" + str(e))

    def outletLocation(self):
        try:
            tier1 = tier2 = tier3 = 0
            if self.oloc == 'tier1':
                tier1 = 1
            elif self.oloc == 'tier2':
                tier2 = 1
            else:
                tier3 = 1
            return {'tier1': tier1, 'tier2': tier2, 'tier3': tier3}
        except Exception as e:
            raise Exception(f"(outletYrs): Something went wrong in transforming Outlet Location\n" + str(e))

    def outletType(self):
        try:
            smkt1 = smkt2 = smkt3 = groc = 0
            if self.otype == 'supermarket1':
                smkt1 = 1
            elif self.otype == 'supermarket2':
                smkt2 = 1
            elif self.otype == 'supermarket3':
                smkt3 = 1
            else:
                groc = 1
            return {'supermarket1': smkt1, 'supermarket2': smkt2, 'supermarket3': smkt3, 'grocery': groc}
        except Exception as e:
            raise Exception(f"(outletYrs): Something went wrong in transforming Outlet Type\n" + str(e))
