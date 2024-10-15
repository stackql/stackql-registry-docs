---
title: appliances_cluster_user_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_cluster_user_credentials
  - resource_connector
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

Creates, updates, deletes, gets or lists a <code>appliances_cluster_user_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appliances_cluster_user_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances_cluster_user_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hybridConnectionConfig" /> | `object` | Contains the REP (rendezvous endpoint) and “Listener” access token from notification service (NS). |
| <CopyableCode code="kubeconfigs" /> | `array` | The list of appliance kubeconfigs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns the cluster user credentials for the dedicated appliance. |

## `SELECT` examples

Returns the cluster user credentials for the dedicated appliance.


```sql
SELECT
hybridConnectionConfig,
kubeconfigs
FROM azure.resource_connector.appliances_cluster_user_credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```