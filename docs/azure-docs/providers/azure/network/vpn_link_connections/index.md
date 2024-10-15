---
title: vpn_link_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections
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

Creates, updates, deletes, gets or lists a <code>vpn_link_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_link_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_link_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnConnection. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_vpn_connection" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all vpn site link connections for a particular virtual wan vpn gateway vpn connection. |
| <CopyableCode code="reset_connection" /> | `EXEC` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Resets the VpnLink connection specified. |
| <CopyableCode code="set_or_init_default_shared_key" /> | `EXEC` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Sets or auto generates the shared key based on the user input. If users give a shared key value, it does the set operation. If key length is given, the operation creates a random key of the pre-defined length. |

## `SELECT` examples

Retrieves all vpn site link connections for a particular virtual wan vpn gateway vpn connection.


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.vpn_link_connections
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```