---
title: subscription_deployment_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_deployment_locations
  - app_service
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

Creates, updates, deletes, gets or lists a <code>subscription_deployment_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_deployment_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.subscription_deployment_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hostingEnvironmentDeploymentInfos" /> | `array` | Available App Service Environments with basic information. |
| <CopyableCode code="hostingEnvironments" /> | `array` | Available App Service Environments with full descriptions of the environments. |
| <CopyableCode code="locations" /> | `array` | Available regions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Gets list of available geo regions plus ministamps |

## `SELECT` examples

Description for Gets list of available geo regions plus ministamps


```sql
SELECT
hostingEnvironmentDeploymentInfos,
hostingEnvironments,
locations
FROM azure.app_service.subscription_deployment_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```