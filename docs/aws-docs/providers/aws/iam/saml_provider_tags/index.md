---
title: saml_provider_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_provider_tags
  - iam
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saml_provider_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.saml_provider_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Key` | `string` | The key name that can be used to look up or retrieve the associated value. For example, &lt;code&gt;Department&lt;/code&gt; or &lt;code&gt;Cost Center&lt;/code&gt; are common choices. |
| `Value` | `string` | &lt;p&gt;The value associated with this tag. For example, tags with a key name of &lt;code&gt;Department&lt;/code&gt; could have values such as &lt;code&gt;Human Resources&lt;/code&gt;, &lt;code&gt;Accounting&lt;/code&gt;, and &lt;code&gt;Support&lt;/code&gt;. Tags with a key name of &lt;code&gt;Cost Center&lt;/code&gt; might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/note&gt; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `saml_provider_tags_List` | `SELECT` | `SAMLProviderArn, region` |
