from opentrons import types
import math

metadata = {
    'protocolName': 'Transfer 384 barcode',
    'author': 'RC',
    'source': 'McGuigan Lab',
    'apiLevel': '2.11'
    }

def run(ctx):

    # 0) load instrument
    tipracks_1 = ctx.load_labware('opentrons_96_tiprack_20ul', '1') #20ul tips
    tipracks_2 = ctx.load_labware('opentrons_96_tiprack_20ul', '3') #20ul tips
    tipracks_3 = ctx.load_labware('opentrons_96_tiprack_20ul', '4') #20ul tips
    tipracks_4 = ctx.load_labware('opentrons_96_tiprack_20ul', '6') #20ul tips
    tip_racks=[tipracks_1,tipracks_2,tipracks_3,tipracks_4]
    left_pip = ctx.load_instrument('p20_multi_gen2', 'left', tip_racks=[tipracks_1,tipracks_2,tipracks_3,tipracks_4])
    right_pip = ctx.load_instrument('p300_multi_gen2', 'right') #p300_multi
    
    masterplate = ctx.load_labware('corning_384_wellplate_112ul_flat', '5')
    source_cells = ctx.load_labware('corning_384_wellplate_112ul_flat', '2')
    
    washing_1 = ctx.load_labware("nest_96_wellplate_2ml_deep", '7')
    washing_2 = ctx.load_labware("nest_96_wellplate_2ml_deep", '8')
    washing_3 = ctx.load_labware("nest_96_wellplate_2ml_deep", '9')
    washing_4 = ctx.load_labware("nest_96_wellplate_2ml_deep", '11')
    washing = [washing_1,washing_2,washing_3,washing_4]

    columns = ['A1','B1','A2','B2','A3','B3','A4','B4','A5','B5','A6','B6','A7','B7','A8','B8','A9','B9','A10','B10','A11','B11','A12','B12','A13','B13','A14','B14','A15','B15','A16','B16','A17','B17','A18','B18','A19','B19','A20','B20','A21','B21','A22','B22','A23','B23','A24','B24']
    
    wash_well = ["A1", "A2", "A3", "A4", "A5", "A6", "A7","A8","A9","A10","A11","A12"]
    
    
    j = 0
    k = 0    
    #Add 5uL barcode into 45uL cell suspension
    for i in range(len(columns)): 
        left_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        left_pip.mix(3, 15, masterplate[columns[i]].bottom(z=1),2)
        left_pip.aspirate(5, masterplate[columns[i]].bottom(z=1))
        left_pip.touch_tip()
        left_pip.dispense(5, source_cells[columns[i]].bottom(z=1))
        left_pip.mix(3,20, source_cells[columns[i]].bottom(z=1), 2)
        left_pip.blow_out()
        left_pip.touch_tip()
        left_pip.return_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0
    
        
    j = 0
    k = 0
    #mix
    for i in range(len(columns)): 
        left_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        left_pip.mix(3, 20, source_cells[columns[i]].bottom(z=1), 3)
        left_pip.blow_out()
        left_pip.touch_tip()
        left_pip.return_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0

    
    
    j = 0
    k = 0
    #Add 20uL PBS-BSA -> wash
    for i in range(len(columns)): 
        left_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        left_pip.aspirate(20, washing[j][wash_well[k]].bottom())
        left_pip.dispense(20, source_cells[columns[i]].bottom(z=3))
        left_pip.blow_out()
        left_pip.touch_tip()
        left_pip.drop_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0

    #Swich to 384_wash_pool protocol
