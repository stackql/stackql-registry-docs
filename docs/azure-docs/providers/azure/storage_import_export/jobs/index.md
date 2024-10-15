---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storage_import_export
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_import_export.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Specifies the resource identifier of the job. |
| <CopyableCode code="name" /> | `text` | Specifies the name of the job. |
| <CopyableCode code="backup_drive_manifest" /> | `text` | field from the `properties` object |
| <CopyableCode code="cancel_requested" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_package" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="drive_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="export" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Specifies the identity properties.  |
| <CopyableCode code="incomplete_blob_list_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Specifies the Azure location where the job is created. |
| <CopyableCode code="log_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="return_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="return_package" /> | `text` | field from the `properties` object |
| <CopyableCode code="return_shipping" /> | `text` | field from the `properties` object |
| <CopyableCode code="shipping_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Specifies the tags that are assigned to the job. |
| <CopyableCode code="type" /> | `text` | Specifies the type of the job resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource identifier of the job. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the job. |
| <CopyableCode code="identity" /> | `object` | Specifies the identity properties.  |
| <CopyableCode code="location" /> | `string` | Specifies the Azure location where the job is created. |
| <CopyableCode code="properties" /> | `object` | Specifies the job properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Specifies the tags that are assigned to the job. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the job resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Gets information about an existing job. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all active and completed jobs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all active and completed jobs in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Creates a new job or updates an existing job in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Deletes an existing job. Only jobs in the Creating or Completed states can be deleted. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job. |

## `SELECT` examples

Returns all active and completed jobs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_drive_manifest,
cancel_requested,
delivery_package,
diagnostics_path,
drive_list,
encryption_key,
export,
identity,
incomplete_blob_list_uri,
jobName,
job_type,
location,
log_level,
percent_complete,
provisioning_state,
resourceGroupName,
return_address,
return_package,
return_shipping,
shipping_information,
state,
storage_account_id,
subscriptionId,
system_data,
tags,
type
FROM azure.storage_import_export.vw_jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
systemData,
tags,
type
FROM azure.storage_import_export.jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO azure.storage_import_export.jobs (
jobName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: storageAccountId
          value: string
        - name: jobType
          value: string
        - name: returnAddress
          value:
            - name: recipientName
              value: string
            - name: streetAddress1
              value: string
            - name: streetAddress2
              value: string
            - name: city
              value: string
            - name: stateOrProvince
              value: string
            - name: postalCode
              value: string
            - name: countryOrRegion
              value: string
            - name: phone
              value: string
            - name: email
              value: string
        - name: returnShipping
          value:
            - name: carrierName
              value: string
            - name: carrierAccountNumber
              value: string
        - name: shippingInformation
          value:
            - name: recipientName
              value: string
            - name: streetAddress1
              value: string
            - name: streetAddress2
              value: string
            - name: city
              value: string
            - name: stateOrProvince
              value: string
            - name: postalCode
              value: string
            - name: countryOrRegion
              value: string
            - name: phone
              value: string
            - name: additionalInformation
              value: string
        - name: deliveryPackage
          value:
            - name: carrierName
              value: string
            - name: trackingNumber
              value: string
            - name: driveCount
              value: integer
            - name: shipDate
              value: string
        - name: returnPackage
          value:
            - name: carrierName
              value: string
            - name: trackingNumber
              value: string
            - name: driveCount
              value: integer
            - name: shipDate
              value: string
        - name: diagnosticsPath
          value: string
        - name: logLevel
          value: string
        - name: backupDriveManifest
          value: boolean
        - name: state
          value: string
        - name: cancelRequested
          value: boolean
        - name: percentComplete
          value: integer
        - name: incompleteBlobListUri
          value: string
        - name: driveList
          value:
            - - name: driveId
                value: string
              - name: bitLockerKey
                value: string
              - name: manifestFile
                value: string
              - name: manifestHash
                value: string
              - name: driveHeaderHash
                value: string
              - name: state
                value: string
              - name: copyStatus
                value: string
              - name: percentComplete
                value: integer
              - name: verboseLogUri
                value: string
              - name: errorLogUri
                value: string
              - name: manifestUri
                value: string
              - name: bytesSucceeded
                value: integer
        - name: export
          value:
            - name: blobList
              value: string
            - name: blobListBlobPath
              value: string
        - name: provisioningState
          value: string
        - name: encryptionKey
          value:
            - name: kekType
              value: string
            - name: kekUrl
              value: string
            - name: kekVaultResourceID
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE azure.storage_import_export.jobs
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_import_export.jobs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
