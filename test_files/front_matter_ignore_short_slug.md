---
key2: value2
slug: tiny-slug
key: value
mdseo-ignore: [chk_fm slug]
---
<DocSection type="function" name="function_with_pep484_type_annotations" module="test_lib.example" heading_level="3">
<SigArgSection>
<SigArg name="param1" type="int" /><SigArg name="param2" type="str" />
</SigArgSection>
<Description summary="Example function with PEP 484 type annotations." extended_summary="The return type must be duplicated in the docstring to comply\nwith the NumPy docstring style." />
<ParamSection name="Parameters">
	<Parameter name="param1" desc="The first parameter." />
	<Parameter name="param2" desc="The second parameter." />
</ParamSection>
<ParamSection name="Returns">
	<Parameter type="bool" desc="True if successful, False otherwise." />
</ParamSection>
</DocSection>

Hello world
