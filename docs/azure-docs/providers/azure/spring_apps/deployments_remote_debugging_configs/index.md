---
title: deployments_remote_debugging_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_remote_debugging_configs
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>deployments_remote_debugging_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_remote_debugging_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.deployments_remote_debugging_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `boolean` | Indicate if remote debugging is enabled |
| <CopyableCode code="port" /> | `integer` | Application debugging port |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Get remote debugging config. |

## `SELECT` examples

Get remote debugging config.


```sql
SELECT
enabled,
port
FROM azure.spring_apps.deployments_remote_debugging_configs
WHERE appName = '{{ appName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```