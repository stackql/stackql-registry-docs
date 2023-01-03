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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dicom_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.dicom_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`. |
| `labels` | `object` | User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| `notificationConfig` | `object` | Specifies where to send notifications upon changes to a data store. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_dicomStores_get` | `SELECT` | `datasetsId, dicomStoresId, locationsId, projectsId` | Gets the specified DICOM store. |
| `projects_locations_datasets_dicomStores_list` | `SELECT` | `datasetsId, locationsId, projectsId` | Lists the DICOM stores in the given dataset. |
| `projects_locations_datasets_dicomStores_create` | `INSERT` | `datasetsId, locationsId, projectsId` | Creates a new DICOM store within the parent dataset. |
| `projects_locations_datasets_dicomStores_delete` | `DELETE` | `datasetsId, dicomStoresId, locationsId, projectsId` | Deletes the specified DICOM store and removes all images that are contained within it. |
| `projects_locations_datasets_dicomStores_deidentify` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | De-identifies data from the source store and writes it to the destination store. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifyDicomStoreSummary. If errors occur, error is set. The LRO result may still be successful if de-identification fails for some DICOM instances. The output DICOM store will not contain these failed resources. Failed resource totals are tracked in Operation.metadata. Error details are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](/healthcare/docs/how-tos/logging)). |
| `projects_locations_datasets_dicomStores_export` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | Exports data to the specified destination by copying it from the DICOM store. Errors are also logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The metadata field type is OperationMetadata. |
| `projects_locations_datasets_dicomStores_import` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | Imports data into the DICOM store by copying it from the specified source. Errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The metadata field type is OperationMetadata. |
| `projects_locations_datasets_dicomStores_patch` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | Updates the specified DICOM store. |
| `projects_locations_datasets_dicomStores_searchForInstances` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | SearchForInstances returns a list of matching instances. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForInstances, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForInstances, see [Searching for studies, series, instances, and frames](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#searching_for_studies_series_instances_and_frames). |
| `projects_locations_datasets_dicomStores_searchForSeries` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | SearchForSeries returns a list of matching series. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForSeries, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForSeries, see [Searching for studies, series, instances, and frames](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#searching_for_studies_series_instances_and_frames). |
| `projects_locations_datasets_dicomStores_searchForStudies` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | SearchForStudies returns a list of matching studies. See [Search Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6). For details on the implementation of SearchForStudies, see [Search transaction](https://cloud.google.com/healthcare/docs/dicom#search_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call SearchForStudies, see [Searching for studies, series, instances, and frames](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#searching_for_studies_series_instances_and_frames). |
| `projects_locations_datasets_dicomStores_storeInstances` | `EXEC` | `datasetsId, dicomStoresId, locationsId, projectsId` | StoreInstances stores DICOM instances associated with study instance unique identifiers (SUID). See [Store Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5). For details on the implementation of StoreInstances, see [Store transaction](https://cloud.google.com/healthcare/docs/dicom#store_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call StoreInstances, see [Storing DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#storing_dicom_data). |
