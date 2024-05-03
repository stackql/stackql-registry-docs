---
title: linode_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - linode_settings
  - managed
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linode_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.linode_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The ID of the Linode these Settings are for.<br /> |
| <CopyableCode code="group" /> | `string` | The group of the Linode these Settings are for. This is for display purposes only.<br /> |
| <CopyableCode code="label" /> | `string` | The label of the Linode these Settings are for.<br /> |
| <CopyableCode code="ssh" /> | `object` | The SSH settings for this Linode.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getManagedLinodeSetting" /> | `SELECT` | <CopyableCode code="linodeId" /> | Returns a single Linode's Managed settings.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="getManagedLinodeSettings" /> | `SELECT` |  | Returns a paginated list of Managed Settings for your Linodes. There will<br />be one entry per Linode on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedLinodeSetting" /> | `EXEC` | <CopyableCode code="linodeId" /> | Returns a single Linode's Managed settings.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedLinodeSettings" /> | `EXEC` |  | Returns a paginated list of Managed Settings for your Linodes. There will<br />be one entry per Linode on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="updateManagedLinodeSetting" /> | `EXEC` | <CopyableCode code="linodeId" /> | Updates a single Linode's Managed settings.<br />This command can only be accessed by the unrestricted users of an account.<br /> |
