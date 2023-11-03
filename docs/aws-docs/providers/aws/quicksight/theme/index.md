---
title: theme
hide_title: false
hide_table_of_contents: false
keywords:
  - theme
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>theme</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>theme</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.theme</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the theme.</p></td></tr><tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BaseThemeId</code></td><td><code>string</code></td><td><p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
				<code>ListThemes</code> or choose <b>Themes</b> from
			within a QuickSight analysis. </p></td></tr><tr><td><code>Configuration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CreatedTime</code></td><td><code>string</code></td><td><p>The date and time that the theme was created.</p></td></tr><tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td><p>The date and time that the theme was last updated.</p></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td><p>A display name for the theme.</p></td></tr><tr><td><code>Permissions</code></td><td><code>array</code></td><td><p>A valid grouping of resource permissions to apply to the new theme.
			</p></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td><p>A map of the key-value pairs for the resource tag or tags that you want to add to the
			resource.</p></td></tr><tr><td><code>ThemeId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Version</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>VersionDescription</code></td><td><code>string</code></td><td><p>A description of the first version of the theme that you're creating. Every time
				<code>UpdateTheme</code> is called, a new version is created. Each version of the
			theme has a description of the version in the <code>VersionDescription</code>
			field.</p></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.theme
WHERE region = 'us-east-1' AND data__Identifier = '{ThemeId}' AND data__Identifier = '{AwsAccountId}'
</pre>
