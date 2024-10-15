---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - app_compliance_automation
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.reports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports', value: 'view', },
        { label: 'reports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cert_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="compliance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_trigger_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_trigger_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger_time" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Create Report's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName" /> | Get the AppComplianceAutomation report and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the AppComplianceAutomation report list for the tenant. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, data__properties" /> | Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName" /> | Delete an AppComplianceAutomation report. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="reportName" /> | Update an exiting AppComplianceAutomation report. |
| <CopyableCode code="fix" /> | `EXEC` | <CopyableCode code="reportName" /> | Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed. |
| <CopyableCode code="nested_resource_check_name_availability" /> | `EXEC` | <CopyableCode code="reportName" /> | Checks the report's nested resource name availability, e.g: Webhooks, Evidences, Snapshots. |
| <CopyableCode code="sync_cert_record" /> | `EXEC` | <CopyableCode code="reportName, data__certRecord" /> | Synchronize attestation record from app compliance. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="reportName" /> | Verify the AppComplianceAutomation report health status. |

## `SELECT` examples

Get the AppComplianceAutomation report list for the tenant.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports', value: 'view', },
        { label: 'reports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cert_records,
compliance_status,
errors,
last_trigger_time,
next_trigger_time,
offer_guid,
provisioning_state,
reportName,
resources,
status,
storage_info,
subscriptions,
tenant_id,
time_zone,
trigger_time
FROM azure_extras.app_compliance_automation.vw_reports
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.app_compliance_automation.reports
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reports</code> resource.

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
INSERT INTO azure_extras.app_compliance_automation.reports (
reportName,
data__properties,
properties
)
SELECT 
'{{ reportName }}',
'{{ data__properties }}',
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
        - name: triggerTime
          value: string
        - name: timeZone
          value: string
        - name: resources
          value:
            - - name: resourceId
                value: string
              - name: resourceType
                value: string
              - name: resourceKind
                value: string
              - name: resourceOrigin
                value: []
              - name: accountId
                value: string
        - name: status
          value: []
        - name: errors
          value:
            - string
        - name: tenantId
          value: string
        - name: offerGuid
          value: string
        - name: nextTriggerTime
          value: string
        - name: lastTriggerTime
          value: string
        - name: subscriptions
          value:
            - string
        - name: complianceStatus
          value:
            - name: m365
              value:
                - name: passedCount
                  value: integer
                - name: failedCount
                  value: integer
                - name: manualCount
                  value: integer
                - name: notApplicableCount
                  value: integer
                - name: pendingCount
                  value: integer
        - name: storageInfo
          value:
            - name: subscriptionId
              value: string
            - name: resourceGroup
              value: string
            - name: accountName
              value: string
            - name: location
              value: string
        - name: certRecords
          value:
            - - name: offerGuid
                value: string
              - name: certificationStatus
                value: string
              - name: ingestionStatus
                value: string
              - name: controls
                value:
                  - - name: controlId
                      value: string
                    - name: controlStatus
                      value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>reports</code> resource.

```sql
/*+ update */
UPDATE azure_extras.app_compliance_automation.reports
SET 
properties = '{{ properties }}'
WHERE 
reportName = '{{ reportName }}';
```

## `DELETE` example

Deletes the specified <code>reports</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.app_compliance_automation.reports
WHERE reportName = '{{ reportName }}';
```
