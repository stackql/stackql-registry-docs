---
title: integration_runtime_nodes_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_nodes_ip_addresses
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>integration_runtime_nodes_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_nodes_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtime_nodes_ip_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipAddress" /> | `string` | The IP address of self-hosted integration runtime node. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, integrationRuntimeName, nodeName, resourceGroupName, subscriptionId" /> | Get the IP address of self-hosted integration runtime node. |

## `SELECT` examples

Get the IP address of self-hosted integration runtime node.


```sql
SELECT
ipAddress
FROM azure.data_factory.integration_runtime_nodes_ip_addresses
WHERE factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND nodeName = '{{ nodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```