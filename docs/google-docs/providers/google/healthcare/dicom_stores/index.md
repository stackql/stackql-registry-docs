---
title: dicom_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - dicom_stores
  - healthcare
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

Creates, updates, deletes or gets an <code>dicom_store</code> resource or lists <code>dicom_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dicom_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.dicom_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`. |
| <CopyableCode code="labels" /> | `object` | User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| <CopyableCode code="notificationConfig" /> | `object` | Specifies where to send notifications upon changes to a data store. |
| <CopyableCode code="streamConfigs" /> | `array` | Optional. A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Gets the specified DICOM store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists the DICOM stores in the given dataset. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Creates a new DICOM store within the parent dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Deletes the specified DICOM store and removes all images that are contained within it. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Updates the specified DICOM store. |
| <CopyableCode code="deidentify" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | De-identifies data from the source store and writes it to the destination store. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifyDicomStoreSummary. If errors occur, error is set. The LRO result may still be successful if de-identification fails for some DICOM instances. The output DICOM store will not contain these failed resources. Failed resource totals are tracked in Operation.metadata. Error details are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Exports data to the specified destination by copying it from the DICOM store. Errors are also logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The metadata field type is OperationMetadata. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Imports data into the DICOM store by copying it from the specified source. Errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The metadata field type is OperationMetadata. |
| <CopyableCode code="search_for_instances" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | SearchForInstances returns a list of matching instances. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForInstances, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForInstances, see [Search for DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#search-dicom). |
| <CopyableCode code="search_for_series" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | SearchForSeries returns a list of matching series. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForSeries, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForSeries, see [Search for DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#search-dicom). |
| <CopyableCode code="search_for_studies" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | SearchForStudies returns a list of matching studies. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForStudies, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForStudies, see [Search for DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#search-dicom). |
| <CopyableCode code="set_blob_storage_settings" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | SetBlobStorageSettings sets the blob storage settings of the specified resources. |
| <CopyableCode code="store_instances" /> | `EXEC` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | StoreInstances stores DICOM instances associated with study instance unique identifiers (SUID). See [Store Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5). For details on the implementation of StoreInstances, see [Store transaction](https://cloud.google.com/healthcare/docs/dicom#store_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call StoreInstances, see [Store DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#store-dicom). |

## `SELECT` examples

Lists the DICOM stores in the given dataset.

```sql
SELECT
name,
labels,
notificationConfig,
streamConfigs
FROM google.healthcare.dicom_stores
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dicom_stores</code> resource.

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
INSERT INTO google.healthcare.dicom_stores (
datasetsId,
locationsId,
projectsId,
name,
notificationConfig,
labels,
streamConfigs
)
SELECT 
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ notificationConfig }}',
'{{ labels }}',
'{{ streamConfigs }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: notificationConfig
        value: '{{ notificationConfig }}'
      - name: labels
        value: '{{ labels }}'
      - name: streamConfigs
        value: '{{ streamConfigs }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a dicom_store only if the necessary resources are available.

```sql
UPDATE google.healthcare.dicom_stores
SET 
name = '{{ name }}',
notificationConfig = '{{ notificationConfig }}',
labels = '{{ labels }}',
streamConfigs = '{{ streamConfigs }}'
WHERE 
datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified dicom_store resource.

```sql
DELETE FROM google.healthcare.dicom_stores
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
