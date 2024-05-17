---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | The tag key. |
| <CopyableCode code="resourceId" /> | `string` | The ID of the resource. |
| <CopyableCode code="resourceType" /> | `string` | The resource type. |
| <CopyableCode code="value" /> | `string` | The tag value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="tags_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes the specified tags for your EC2 resources.&lt;/p&gt; &lt;p&gt;For more information about tags, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html"&gt;Tagging Your Resources&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="tags_Create" /> | `INSERT` | <CopyableCode code="ResourceId, Tag, region" /> | &lt;p&gt;Adds or overwrites only the specified tags for the specified Amazon EC2 resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource.&lt;/p&gt; &lt;p&gt;For more information about tags, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html"&gt;Tagging Your Resources&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. For more information about creating IAM policies that control users' access to resources based on tags, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html"&gt;Supported Resource-Level Permissions for Amazon EC2 API Actions&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="tags_Delete" /> | `DELETE` | <CopyableCode code="ResourceId, region" /> | &lt;p&gt;Deletes the specified set of tags from the specified set of resources.&lt;/p&gt; &lt;p&gt;To list the current tags, use &lt;a&gt;DescribeTags&lt;/a&gt;. For more information about tags, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html"&gt;Tagging Your Resources&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
