---
title: clusters_gateway_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_gateway_settings
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>clusters_gateway_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_gateway_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.clusters_gateway_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="restAuthCredential.isEnabled" /> | `string` | Indicates whether or not the gateway settings based authorization is enabled. |
| <CopyableCode code="restAuthCredential.password" /> | `string` | The gateway settings user password. |
| <CopyableCode code="restAuthCredential.username" /> | `string` | The gateway settings user name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets the gateway settings for the specified cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Configures the gateway settings on the specified cluster. |

## `SELECT` examples

Gets the gateway settings for the specified cluster.


```sql
SELECT
restAuthCredential.isEnabled,
restAuthCredential.password,
restAuthCredential.username
FROM azure.hdinsight.clusters_gateway_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```