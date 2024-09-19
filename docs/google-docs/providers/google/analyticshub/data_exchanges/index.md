---
title: data_exchanges
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exchanges
  - analyticshub
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

Creates, updates, deletes, gets or lists a <code>data_exchanges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_exchanges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.analyticshub.data_exchanges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the data exchange. e.g. `projects/myproject/locations/US/dataExchanges/123`. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. |
| <CopyableCode code="discoveryType" /> | `string` | Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange. |
| <CopyableCode code="displayName" /> | `string` | Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. |
| <CopyableCode code="documentation" /> | `string` | Optional. Documentation describing the data exchange. |
| <CopyableCode code="icon" /> | `string` | Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. |
| <CopyableCode code="listingCount" /> | `integer` | Output only. Number of listings contained in the data exchange. |
| <CopyableCode code="primaryContact" /> | `string` | Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. |
| <CopyableCode code="sharingEnvironmentConfig" /> | `object` | Sharing environment is a behavior model for sharing data within a data exchange. This option is configurable for a data exchange. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_data_exchanges_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists all data exchanges from projects in a given organization and location. |
| <CopyableCode code="projects_locations_data_exchanges_get" /> | `SELECT` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Gets the details of a data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all data exchanges in a given project and location. |
| <CopyableCode code="projects_locations_data_exchanges_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_delete" /> | `DELETE` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Deletes an existing data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_patch" /> | `UPDATE` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Updates an existing data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_subscribe" /> | `EXEC` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. |

## `SELECT` examples

Lists all data exchanges in a given project and location.

```sql
SELECT
name,
description,
discoveryType,
displayName,
documentation,
icon,
listingCount,
primaryContact,
sharingEnvironmentConfig
FROM google.analyticshub.data_exchanges
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_exchanges</code> resource.

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
INSERT INTO google.analyticshub.data_exchanges (
locationsId,
projectsId,
displayName,
description,
primaryContact,
documentation,
icon,
sharingEnvironmentConfig,
discoveryType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ description }}',
'{{ primaryContact }}',
'{{ documentation }}',
'{{ icon }}',
'{{ sharingEnvironmentConfig }}',
'{{ discoveryType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: primaryContact
      value: string
    - name: documentation
      value: string
    - name: listingCount
      value: integer
    - name: icon
      value: string
    - name: sharingEnvironmentConfig
      value:
        - name: defaultExchangeConfig
          value: []
        - name: dcrExchangeConfig
          value:
            - name: singleSelectedResourceSharingRestriction
              value: boolean
            - name: singleLinkedDatasetPerCleanroom
              value: boolean
    - name: discoveryType
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_exchanges</code> resource.

```sql
/*+ update */
UPDATE google.analyticshub.data_exchanges
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
primaryContact = '{{ primaryContact }}',
documentation = '{{ documentation }}',
icon = '{{ icon }}',
sharingEnvironmentConfig = '{{ sharingEnvironmentConfig }}',
discoveryType = '{{ discoveryType }}'
WHERE 
dataExchangesId = '{{ dataExchangesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>data_exchanges</code> resource.

```sql
/*+ delete */
DELETE FROM google.analyticshub.data_exchanges
WHERE dataExchangesId = '{{ dataExchangesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
