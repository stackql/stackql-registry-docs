---
title: build_service_builder_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builder_deployments
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

Creates, updates, deletes, gets or lists a <code>build_service_builder_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_builder_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_builder_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deployments" /> | `array` | A list of deployment resource ids. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | List deployments that are using the builder. |

## `SELECT` examples

List deployments that are using the builder.


```sql
SELECT
deployments
FROM azure.spring_apps.build_service_builder_deployments
WHERE buildServiceName = '{{ buildServiceName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```