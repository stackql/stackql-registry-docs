---
title: managed_prefix_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_prefix_lists
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
<tr><td><b>Name</b></td><td><code>managed_prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.managed_prefix_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addressFamily" /> | `string` | The IP address version. |
| <CopyableCode code="maxEntries" /> | `integer` | The maximum number of entries for the prefix list. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the owner of the prefix list. |
| <CopyableCode code="prefixListArn" /> | `string` | The Amazon Resource Name (ARN) for the prefix list. |
| <CopyableCode code="prefixListId" /> | `string` | The ID of the prefix list. |
| <CopyableCode code="prefixListName" /> | `string` | The name of the prefix list. |
| <CopyableCode code="state" /> | `string` | The current state of the prefix list. |
| <CopyableCode code="stateMessage" /> | `string` | The state message. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the prefix list. |
| <CopyableCode code="version" /> | `integer` | The version of the prefix list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="managed_prefix_lists_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes your managed prefix lists and any Amazon Web Services-managed prefix lists.&lt;/p&gt; &lt;p&gt;To view the entries for your prefix list, use &lt;a&gt;GetManagedPrefixListEntries&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="managed_prefix_list_Create" /> | `INSERT` | <CopyableCode code="AddressFamily, MaxEntries, PrefixListName, region" /> | Creates a managed prefix list. You can specify one or more entries for the prefix list. Each entry consists of a CIDR block and an optional description. |
| <CopyableCode code="managed_prefix_list_Delete" /> | `DELETE` | <CopyableCode code="PrefixListId, region" /> | Deletes the specified managed prefix list. You must first remove all references to the prefix list in your resources. |
| <CopyableCode code="managed_prefix_list_Modify" /> | `EXEC` | <CopyableCode code="PrefixListId, region" /> | &lt;p&gt;Modifies the specified managed prefix list.&lt;/p&gt; &lt;p&gt;Adding or removing entries in a prefix list creates a new version of the prefix list. Changing the name of the prefix list does not affect the version.&lt;/p&gt; &lt;p&gt;If you specify a current version number that does not match the true current version number, the request fails.&lt;/p&gt; |
