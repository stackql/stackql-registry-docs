---
title: applications_business_process_development_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_business_process_development_artifacts
  - integration_environment
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

Creates, updates, deletes, gets or lists a <code>applications_business_process_development_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications_business_process_development_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.applications_business_process_development_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the business process development artifact. |
| <CopyableCode code="properties" /> | `object` | The properties of business process development artifact. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The get business process development artifact action. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | The list business process development artifacts action. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The delete business process development artifact action. |

## `SELECT` examples

The list business process development artifacts action.


```sql
SELECT
name,
properties,
systemData
FROM azure.integration_environment.applications_business_process_development_artifacts
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>applications_business_process_development_artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.integration_environment.applications_business_process_development_artifacts
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__name = '{{ data__name }}';
```
