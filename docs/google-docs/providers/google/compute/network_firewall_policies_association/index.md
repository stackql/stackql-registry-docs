---
title: network_firewall_policies_association
hide_title: false
hide_table_of_contents: false
keywords:
  - network_firewall_policies_association
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_firewall_policies_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.network_firewall_policies_association" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name for an association. |
| <CopyableCode code="attachmentTarget" /> | `string` | The target that the firewall policy is attached to. |
| <CopyableCode code="displayName" /> | `string` | [Output Only] Deprecated, please use short name instead. The display name of the firewall policy of the association. |
| <CopyableCode code="firewallPolicyId" /> | `string` | [Output Only] The firewall policy ID of the association. |
| <CopyableCode code="shortName" /> | `string` | [Output Only] The short name of the firewall policy of the association. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_association" /> | `SELECT` | <CopyableCode code="firewallPolicy, project" /> | Gets an association with the specified name. |
| <CopyableCode code="add_association" /> | `EXEC` | <CopyableCode code="firewallPolicy, project" /> | Inserts an association for the specified firewall policy. |
| <CopyableCode code="remove_association" /> | `EXEC` | <CopyableCode code="firewallPolicy, project" /> | Removes an association for the specified firewall policy. |
