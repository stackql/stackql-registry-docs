---
title: deployment_info
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_info
  - elastic
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

Creates, updates, deletes, gets or lists a <code>deployment_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.deployment_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deploymentUrl" /> | `string` | Deployment URL of the elasticsearch in Elastic cloud deployment. |
| <CopyableCode code="diskCapacity" /> | `string` | Disk capacity of the elasticsearch in Elastic cloud deployment. |
| <CopyableCode code="elasticsearchEndPoint" /> | `string` | Elasticsearch endpoint in Elastic cloud deployment. This is either the aliased_endpoint if available, or the service_url otherwise. |
| <CopyableCode code="marketplaceSaasInfo" /> | `object` | Marketplace SAAS Info of the resource. |
| <CopyableCode code="memoryCapacity" /> | `string` | RAM capacity of the elasticsearch in Elastic cloud deployment. |
| <CopyableCode code="status" /> | `string` | Flag specifying if the Elastic deployment status is healthy or not. |
| <CopyableCode code="version" /> | `string` | Version of the elasticsearch in Elastic cloud deployment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
deploymentUrl,
diskCapacity,
elasticsearchEndPoint,
marketplaceSaasInfo,
memoryCapacity,
status,
version
FROM azure_isv.elastic.deployment_info
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```