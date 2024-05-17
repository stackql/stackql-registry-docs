---
title: prefix_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_lists
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
<tr><td><b>Name</b></td><td><code>prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.prefix_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cidrSet" /> | `array` | The IP address range of the Amazon Web Service. |
| <CopyableCode code="prefixListId" /> | `string` | The ID of the prefix. |
| <CopyableCode code="prefixListName" /> | `string` | The name of the prefix. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="prefix_lists_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
