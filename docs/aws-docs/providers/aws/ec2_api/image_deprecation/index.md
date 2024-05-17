---
title: image_deprecation
hide_title: false
hide_table_of_contents: false
keywords:
  - image_deprecation
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
<tr><td><b>Name</b></td><td><code>image_deprecation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.image_deprecation" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="image_deprecation_Disable" /> | `EXEC` | <CopyableCode code="ImageId, region" /> | &lt;p&gt;Cancels the deprecation of the specified AMI.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html"&gt;Deprecate an AMI&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="image_deprecation_Enable" /> | `EXEC` | <CopyableCode code="DeprecateAt, ImageId, region" /> | &lt;p&gt;Enables deprecation of the specified AMI at the specified date and time.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html"&gt;Deprecate an AMI&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
