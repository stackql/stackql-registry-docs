---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - firestore
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firestore.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databases" /> | `array` | The databases in the project. |
| <CopyableCode code="unreachable" /> | `array` | In the event that data about individual databases cannot be listed they will be recorded here. An example entry might be: projects/some_project/locations/some_location This can happen if the Cloud Region that the Database resides in is currently unavailable. In this case we can't fetch all the details about the database. You may be able to get a more detailed error message (or possibly fetch the resource) by sending a 'Get' request for the resource or a 'List' request for the specific location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databasesId, projectsId" /> | Gets information about a database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | List all the databases in the project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create a database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databasesId, projectsId" /> | Deletes a database. |
| <CopyableCode code="export_documents" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: https://cloud.google.com/firestore/docs/manage-data/export-import |
| <CopyableCode code="import_documents" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Updates a database. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="projectsId" /> | Creates a new database by restoring from an existing backup. The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup. The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed. |
