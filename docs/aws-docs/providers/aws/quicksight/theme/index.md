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
<tr><td><b>Description</b></td><td>theme</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.theme</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the theme.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_theme_id</code></td><td><code>string</code></td><td>&lt;p&gt;The ID of the theme that a custom theme will inherit from. All themes inherit from one of&lt;br&#x2F;&gt;			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use&lt;br&#x2F;&gt;				&lt;code&gt;ListThemes&lt;&#x2F;code&gt; or choose &lt;b&gt;Themes&lt;&#x2F;b&gt; from&lt;br&#x2F;&gt;			within a QuickSight analysis. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time that the theme was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time that the theme was last updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>&lt;p&gt;A display name for the theme.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td>&lt;p&gt;A valid grouping of resource permissions to apply to the new theme.&lt;br&#x2F;&gt;			&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;A map of the key-value pairs for the resource tag or tags that you want to add to the&lt;br&#x2F;&gt;			resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>theme_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td>&lt;p&gt;A description of the first version of the theme that you're creating. Every time&lt;br&#x2F;&gt;				&lt;code&gt;UpdateTheme&lt;&#x2F;code&gt; is called, a new version is created. Each version of the&lt;br&#x2F;&gt;			theme has a description of the version in the &lt;code&gt;VersionDescription&lt;&#x2F;code&gt;&lt;br&#x2F;&gt;			field.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
aws_account_id,
base_theme_id,
configuration,
created_time,
last_updated_time,
name,
permissions,
tags,
theme_id,
type,
version,
version_description
FROM aws.quicksight.theme
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ThemeId&gt;'
AND data__Identifier = '&lt;AwsAccountId&gt;'
```
