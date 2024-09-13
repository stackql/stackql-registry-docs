---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes or gets an <code>dataset</code> resource or lists <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the dataset, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a resource. |
| <CopyableCode code="timeZone" /> | `string` | Optional. The default timezone used by this dataset. Must be a either a valid IANA time zone name such as "America/New_York" or empty, which defaults to UTC. This is used for parsing times in resources, such as HL7 messages, where no explicit timezone is specified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Gets any metadata associated with a dataset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the health datasets in the current project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new health dataset. Results are returned through the Operation interface which returns either an `Operation.response` which contains a Dataset or `Operation.error`. The metadata field type is OperationMetadata. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Deletes the specified health dataset and all data contained in the dataset. Deleting a dataset does not affect the sources from which the dataset was imported (if any). |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Updates dataset metadata. |
| <CopyableCode code="deidentify" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Creates a new dataset containing de-identified data from the source dataset. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifySummary. If errors occur, error is set. The LRO result may still be successful if de-identification fails for some DICOM instances. The new de-identified dataset will not contain these failed resources. Failed resource totals are tracked in Operation.metadata. Error details are also logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). |

## `SELECT` examples

Lists the health datasets in the current project.

```sql
SELECT
name,
encryptionSpec,
timeZone
FROM google.healthcare.datasets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datasets</code> resource.

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
INSERT INTO google.healthcare.datasets (
locationsId,
projectsId,
name,
timeZone,
encryptionSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ timeZone }}',
'{{ encryptionSpec }}'
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
      - name: timeZone
        value: '{{ timeZone }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a dataset only if the necessary resources are available.

```sql
UPDATE google.healthcare.datasets
SET 
name = '{{ name }}',
timeZone = '{{ timeZone }}',
encryptionSpec = '{{ encryptionSpec }}'
WHERE 
datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified dataset resource.

```sql
DELETE FROM google.healthcare.datasets
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
