---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - servicemanagement
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicemanagement.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="producerProjectId" /> | `string` | ID of the project that produces and owns this service. |
| <CopyableCode code="serviceName" /> | `string` | The name of the service. See the [overview](https://cloud.google.com/service-infrastructure/docs/overview) for naming requirements. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets a managed service. Authentication is required unless the service is public. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists managed services. Returns all public services. For authenticated users, also returns all services the calling user has "servicemanagement.services.get" permission for. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a new managed service. A managed service is immutable, and is subject to mandatory 30-day data retention. You cannot move a service or recreate it within 30 days after deletion. One producer project can own no more than 500 services. For security and reliability purposes, a production service should be hosted in a dedicated producer project. Operation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="serviceName" /> | Deletes a managed service. This method will change the service to the `Soft-Delete` state for 30 days. Within this period, service producers may call UndeleteService to restore the service. After 30 days, the service will be permanently deleted. Operation |
| <CopyableCode code="generate_config_report" /> | `EXEC` | <CopyableCode code="" /> | Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_value If GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value. If GenerateConfigReportRequest.old_value is not specified, this method will compare GenerateConfigReportRequest.new_value with the last pushed service configuration. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="serviceName" /> | Revives a previously deleted managed service. The method restores the service using the configuration at the time the service was deleted. The target service must exist and must have been deleted within the last 30 days. Operation |

## `SELECT` examples

Lists managed services. Returns all public services. For authenticated users, also returns all services the calling user has "servicemanagement.services.get" permission for.

```sql
SELECT
producerProjectId,
serviceName
FROM google.servicemanagement.services
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.servicemanagement.services (
,
serviceName,
producerProjectId
)
SELECT 
'{{  }}',
'{{ serviceName }}',
'{{ producerProjectId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
serviceName: string
producerProjectId: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM google.servicemanagement.services
WHERE serviceName = '{{ serviceName }}';
```
