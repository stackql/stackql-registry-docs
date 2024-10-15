---
title: vpn_link_connections_all_shared_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections_all_shared_keys
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

Creates, updates, deletes, gets or lists a <code>vpn_link_connections_all_shared_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_link_connections_all_shared_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_link_connections_all_shared_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Parameters for SharedKey. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Lists all shared keys of VpnLink connection specified. |

## `SELECT` examples

Lists all shared keys of VpnLink connection specified.


```sql
SELECT
id,
name,
properties,
type
FROM azure.network.vpn_link_connections_all_shared_keys
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND linkConnectionName = '{{ linkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```