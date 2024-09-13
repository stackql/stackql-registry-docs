---
title: domain_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_mappings
  - appengine
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

Creates, updates, deletes or gets an <code>domain_mapping</code> resource or lists <code>domain_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.domain_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Relative name of the domain serving the application. Example: example.com. |
| <CopyableCode code="name" /> | `string` | Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.@OutputOnly |
| <CopyableCode code="resourceRecords" /> | `array` | The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping.@OutputOnly |
| <CopyableCode code="sslSettings" /> | `object` | SSL configuration for a DomainMapping resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, domainMappingsId" /> | Gets the specified domain mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId" /> | Lists the domain mappings on an application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appsId" /> | Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, domainMappingsId" /> | Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId, domainMappingsId" /> | Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource. |

## `SELECT` examples

Lists the domain mappings on an application.

```sql
SELECT
id,
name,
resourceRecords,
sslSettings
FROM google.appengine.domain_mappings
WHERE appsId = '{{ appsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_mappings</code> resource.

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
INSERT INTO google.appengine.domain_mappings (
appsId,
name,
id,
sslSettings,
resourceRecords
)
SELECT 
'{{ appsId }}',
'{{ name }}',
'{{ id }}',
'{{ sslSettings }}',
'{{ resourceRecords }}'
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
      - name: id
        value: '{{ id }}'
      - name: sslSettings
        value: '{{ sslSettings }}'
      - name: resourceRecords
        value: '{{ resourceRecords }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a domain_mapping only if the necessary resources are available.

```sql
UPDATE google.appengine.domain_mappings
SET 
name = '{{ name }}',
id = '{{ id }}',
sslSettings = '{{ sslSettings }}',
resourceRecords = '{{ resourceRecords }}'
WHERE 
appsId = '{{ appsId }}'
AND domainMappingsId = '{{ domainMappingsId }}';
```

## `DELETE` example

Deletes the specified domain_mapping resource.

```sql
DELETE FROM google.appengine.domain_mappings
WHERE appsId = '{{ appsId }}'
AND domainMappingsId = '{{ domainMappingsId }}';
```
