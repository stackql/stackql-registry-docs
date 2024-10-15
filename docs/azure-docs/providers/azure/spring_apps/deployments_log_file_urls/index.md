---
title: deployments_log_file_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_log_file_urls
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

Creates, updates, deletes, gets or lists a <code>deployments_log_file_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_log_file_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.deployments_log_file_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="url" /> | `string` | URL of the log file |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Get deployment log file URL |

## `SELECT` examples

Get deployment log file URL


```sql
SELECT
url
FROM azure.spring_apps.deployments_log_file_urls
WHERE appName = '{{ appName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```