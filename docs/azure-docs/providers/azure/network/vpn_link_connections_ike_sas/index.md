---
title: vpn_link_connections_ike_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections_ike_sas
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

Creates, updates, deletes, gets or lists a <code>vpn_link_connections_ike_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_link_connections_ike_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_link_connections_ike_sas" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Lists IKE Security Associations for Vpn Site Link Connection in the specified resource group. |

## `SELECT` examples

Lists IKE Security Associations for Vpn Site Link Connection in the specified resource group.


```sql
SELECT

FROM azure.network.vpn_link_connections_ike_sas
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND linkConnectionName = '{{ linkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```