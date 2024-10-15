---
title: group_quota_limits_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_limits_requests
  - quota
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

Creates, updates, deletes, gets or lists a <code>group_quota_limits_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_limits_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_limits_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, requestId" /> | Get API to check the status of a GroupQuota request by requestId. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceProviderName" /> | Get API to check the status of a GroupQuota request by requestId. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Put the GroupQuota requests for a specific ResourceProvider/Location/Resource. the location and resourceName ("name": {"value" : "resourceName") properties are specified in the request body. Only 1 resource quota can be requested.
Use the polling API - OperationsStatus URI specified in Azure-AsyncOperation header field, with retry-after duration in seconds to check the intermediate status. This API provides the finals status with the request details and status. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Create the GroupQuota requests for a specific ResourceProvider/Location/Resource. the location and resourceName properties are specified in the request body. Only 1 resource quota can be requested. Please note that patch request creates a new groupQuota request.
Use the polling API - OperationsStatus URI specified in Azure-AsyncOperation header field, with retry-after duration in seconds to check the intermediate status. This API provides the finals status with the request details and status. |

## `SELECT` examples

Get API to check the status of a GroupQuota request by requestId.


```sql
SELECT
properties
FROM azure.quota.group_quota_limits_requests
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND requestId = '{{ requestId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_quota_limits_requests</code> resource.

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
INSERT INTO azure.quota.group_quota_limits_requests (
groupQuotaName,
managementGroupId,
resourceName,
resourceProviderName,
properties
)
SELECT 
'{{ groupQuotaName }}',
'{{ managementGroupId }}',
'{{ resourceName }}',
'{{ resourceProviderName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: requestedResource
          value:
            - name: properties
              value:
                - name: limit
                  value: integer
                - name: name
                  value:
                    - name: value
                      value: string
                    - name: localizedValue
                      value: string
                - name: region
                  value: []
                - name: comments
                  value: string
        - name: requestSubmitTime
          value: string
        - name: provisioningState
          value: []
        - name: faultCode
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>group_quota_limits_requests</code> resource.

```sql
/*+ update */
UPDATE azure.quota.group_quota_limits_requests
SET 
properties = '{{ properties }}'
WHERE 
groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND resourceName = '{{ resourceName }}'
AND resourceProviderName = '{{ resourceProviderName }}';
```
