---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - network
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation, as per Resource-Based Access Control (RBAC). Examples: "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action" |
| <CopyableCode code="actionType" /> | `string` | Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs. |
| <CopyableCode code="display" /> | `object` | Localized display information for this particular operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Whether the operation applies to data-plane. This is "true" for data-plane operations and "false" for ARM/control-plane operations. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit logs UX. Default value is "user,system" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available Network Rest API operations. |
| <CopyableCode code="check_dns_name_availability" /> | `EXEC` | <CopyableCode code="domainNameLabel, location, subscriptionId" /> | Checks whether a domain name in the cloudapp.azure.com zone is available for use. |
| <CopyableCode code="disconnect_active_sessions" /> | `EXEC` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Returns the list of currently active sessions on the Bastion. |
| <CopyableCode code="express_route_provider_port" /> | `EXEC` | <CopyableCode code="providerport, subscriptionId" /> | Retrieves detail of a provider port. |
| <CopyableCode code="generatevirtualwanvpnserverconfigurationvpnprofile" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualWANName" /> | Generates a unique VPN profile for P2S clients for VirtualWan and associated VpnServerConfiguration combination in the specified resource group. |
| <CopyableCode code="supported_security_providers" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualWANName" /> | Gives the supported security providers for the virtual wan. |

## `SELECT` examples

Lists all of the available Network Rest API operations.


```sql
SELECT
name,
actionType,
display,
isDataAction,
origin
FROM azure.network.operations
;
```