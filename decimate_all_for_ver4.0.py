bl_info = {
    "name": "DecimateAll_for4.0",
    "author": "Shuya Tamaru",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "View3D > Sidebar",
    "description": "Decimate all object and apply",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

import bpy


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "DecimateAll"
    bl_idname = "OBJECT_PT_DecimateAll"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "DecimateAll_for4.0"

    def draw(self, context):
        self.layout.row().operator("object.simple_operator")


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "DecimateAll_for4.0"

    def execute(self, context):
        for object1 in bpy.data.objects:
            if object1.type == 'MESH':
                mod = object1.modifiers.new("DECIMATE", "DECIMATE")
                mod.decimate_type = 'DISSOLVE'
                # Apply the modifier
                bpy.context.view_layer.objects.active = object1
                bpy.ops.object.modifier_apply(modifier=mod.name)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(SimpleOperator)
    
if __name__ == "__main__":
    register()