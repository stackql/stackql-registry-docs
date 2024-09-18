---
title: peered_dns_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - peered_dns_domains
  - servicenetworking
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

Creates, updates, deletes, gets or lists a <code>peered_dns_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peered_dns_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.peered_dns_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="peeredDnsDomains" /> | `array` | The list of peered DNS domains. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> | Lists peered DNS domains for a connection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networksId, projectsId, servicesId" /> | Creates a peered DNS domain which sends requests for records in given namespace originating in the service producer VPC network to the consumer VPC network to be resolved. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networksId, peeredDnsDomainsId, projectsId, servicesId" /> | Deletes a peered DNS domain. |

## `SELECT` examples

Lists peered DNS domains for a connection.

```sql
SELECT
peeredDnsDomains
FROM google.servicenetworking.peered_dns_domains
WHERE networksId = '{{ networksId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peered_dns_domains</code> resource.

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
INSERT INTO google.servicenetworking.peered_dns_domains (
networksId,
projectsId,
servicesId,
name,
dnsSuffix
)
SELECT 
'{{ networksId }}',
'{{ projectsId }}',
'{{ servicesId }}',
'{{ name }}',
'{{ dnsSuffix }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
dnsSuffix: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>peered_dns_domains</code> resource.

```sql
/*+ delete */
DELETE FROM google.servicenetworking.peered_dns_domains
WHERE networksId = '{{ networksId }}'
AND peeredDnsDomainsId = '{{ peeredDnsDomainsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
