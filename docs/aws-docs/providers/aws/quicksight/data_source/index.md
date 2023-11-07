---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
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
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.quicksight.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AlternateDataSourceParameters</code></td><td><code>array</code></td><td>&lt;p&gt;A set of alternate data source parameters that you want to share for the credentials&lt;br&#x2F;&gt;            stored with this data source. The credentials are applied in tandem with the data source&lt;br&#x2F;&gt;            parameters when you copy a data source by using a create or update request. The API&lt;br&#x2F;&gt;            operation compares the &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt; structure that's in the request&lt;br&#x2F;&gt;            with the structures in the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; allow list. If the&lt;br&#x2F;&gt;            structures are an exact match, the request is allowed to use the credentials from this&lt;br&#x2F;&gt;            existing data source. If the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; list is null,&lt;br&#x2F;&gt;            the &lt;code&gt;Credentials&lt;&#x2F;code&gt; originally used with this &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt;&lt;br&#x2F;&gt;            are automatically allowed.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>&lt;p&gt;The time that this data source was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Credentials</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataSourceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataSourceParameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ErrorInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td>&lt;p&gt;The last time that this data source was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>&lt;p&gt;A display name for the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Permissions</code></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>SslProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VpcConnectionProperties</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.data_source
WHERE region = 'us-east-1' AND data__Identifier = '&lt;AwsAccountId&gt;' AND data__Identifier = '&lt;DataSourceId&gt;'
</pre>
