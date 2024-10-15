---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>incidents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incidents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incidents', value: 'view', },
        { label: 'incidents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="classification" /> | `text` | field from the `properties` object |
| <CopyableCode code="classification_comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="classification_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="first_activity_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="incidentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="incident_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="incident_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_activity_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_incident_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_analytic_rule_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes incident properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all incidents. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a given incident. |
| <CopyableCode code="run_playbook" /> | `EXEC` | <CopyableCode code="incidentIdentifier, resourceGroupName, subscriptionId, workspaceName, data__logicAppsResourceId" /> | Triggers playbook on a specific incident |

## `SELECT` examples

Gets all incidents.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incidents', value: 'view', },
        { label: 'incidents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
additional_data,
classification,
classification_comment,
classification_reason,
created_time_utc,
etag,
first_activity_time_utc,
incidentId,
incident_number,
incident_url,
labels,
last_activity_time_utc,
last_modified_time_utc,
owner,
provider_incident_id,
provider_name,
related_analytic_rule_ids,
resourceGroupName,
severity,
status,
subscriptionId,
title,
workspaceName
FROM azure.sentinel.vw_incidents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.incidents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>incidents</code> resource.

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
INSERT INTO azure.sentinel.incidents (
incidentId,
resourceGroupName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ incidentId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: additionalData
          value:
            - name: alertsCount
              value: integer
            - name: bookmarksCount
              value: integer
            - name: commentsCount
              value: integer
            - name: alertProductNames
              value:
                - string
            - name: tactics
              value:
                - []
            - name: providerIncidentUrl
              value: string
        - name: classification
          value: string
        - name: classificationComment
          value: string
        - name: classificationReason
          value: string
        - name: createdTimeUtc
          value: string
        - name: description
          value: string
        - name: firstActivityTimeUtc
          value: string
        - name: incidentUrl
          value: string
        - name: providerName
          value: string
        - name: providerIncidentId
          value: string
        - name: incidentNumber
          value: integer
        - name: labels
          value:
            - - name: labelName
                value: string
              - name: labelType
                value: []
        - name: lastActivityTimeUtc
          value: string
        - name: lastModifiedTimeUtc
          value: string
        - name: owner
          value:
            - name: email
              value: string
            - name: assignedTo
              value: string
            - name: objectId
              value: string
            - name: userPrincipalName
              value: string
            - name: ownerType
              value: string
        - name: relatedAnalyticRuleIds
          value:
            - string
        - name: severity
          value: []
        - name: status
          value: string
        - name: title
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>incidents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.incidents
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
