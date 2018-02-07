# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Sculpt Symmetry Pie Menu",
           "author": "CDMJ",
           "version": (1, 0, 0),
           "blender": (2, 79, 0),
           "location": "",
           "description": "Symmetry in Sculpt Toggle Pie on Y key",
           "warning": "Sculpt Mode Only",
           "category": "3D View"}






import bpy
from bpy.types import Menu

#operators

#one
class OperOne(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_one"
    bl_label = "X Axis Toggle"

    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')

    def execute(self, context):
        sculpt_var = bpy.context.scene.tool_settings.sculpt
        if sculpt_var.use_symmetry_x == False:
            
            sculpt_var.use_symmetry_x = True
        else:
            sculpt_var.use_symmetry_x = False
            
        return {'FINISHED'}
    
#two   
class OperTwo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_two"
    bl_label = "Y Axis Toggle"

    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')

    def execute(self, context):
        sculpt_var = bpy.context.scene.tool_settings.sculpt
        if sculpt_var.use_symmetry_y == False:
            
            sculpt_var.use_symmetry_y = True
        else:
            sculpt_var.use_symmetry_y = False
        return {'FINISHED'}

#three
class OperThree(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_three"
    bl_label = "Asymmetric"

    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')

    def execute(self, context):
        sculpt_var = bpy.context.scene.tool_settings.sculpt
        sculpt_var.use_symmetry_x = False
        sculpt_var.use_symmetry_y = False
        sculpt_var.use_symmetry_z = False
        
        return {'FINISHED'}
    
#four
class OperFour(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_four"
    bl_label = "Z Axis Toggle"
 
    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')
 
    def execute(self, context):
        sculpt_var = bpy.context.scene.tool_settings.sculpt
        if sculpt_var.use_symmetry_z == False:
            
            sculpt_var.use_symmetry_z = True
        else:
            sculpt_var.use_symmetry_z = False
        return {'FINISHED'}

    
    
    
#------------------------------------#pie
class VIEW3D_PIE_sculptsymmetry(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Sculpt Symmetry"
    
    

    def draw(self, context):
        layout = self.layout
        
        pie = layout.menu_pie()
        #pie.operator("render.render", text='one')

        pie.operator("object.oper_one", text='Toggle X Axis', icon='MANIPUL')
        pie.operator("object.oper_two", text='Toggle Y Axis', icon='MANIPUL')
        pie.operator("object.oper_three", text='Asymmetric', icon='MANIPUL')
        pie.operator("object.oper_four", text='Toggle Z Axis', icon='MANIPUL')
        
        
        
def register():
    bpy.utils.register_module(__name__)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Y', 'PRESS') 
        kmi.properties.name = "VIEW3D_PIE_sculptsymmetry"

def unregister():
    bpy.utils.unregister_module(__name__)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items \
                            if (kmi.idname == "VIEW3D_PIE_sculptsymmetry")):
            km.keymap_items.remove(kmi)
        







if __name__ == "__main__":
    register()
