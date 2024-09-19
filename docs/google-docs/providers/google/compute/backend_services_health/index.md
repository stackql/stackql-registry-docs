---
title: backend_services_health
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_services_health
  - compute
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

Creates, updates, deletes, gets or lists a <code>backend_services_health</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backend_services_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.backend_services_health" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotations" /> | `object` | Metadata defined as annotations on the network endpoint group. |
| <CopyableCode code="healthStatus" /> | `array` | Health state of the backend instances or endpoints in requested instance or network endpoint group, determined based on configured health checks. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#backendServiceGroupHealth for the health of backend services. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_health" /> | `SELECT` | <CopyableCode code="backendService, project" /> | Gets the most recent health check results for this BackendService. Example request body: { "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" } |

## `SELECT` examples

Gets the most recent health check results for this BackendService. Example request body: { "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" }

```sql
SELECT
annotations,
healthStatus,
kind
FROM google.compute.backend_services_health
WHERE backendService = '{{ backendService }}'
AND project = '{{ project }}';
```
