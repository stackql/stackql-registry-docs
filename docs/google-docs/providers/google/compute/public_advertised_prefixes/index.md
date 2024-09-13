
---
title: public_advertised_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - public_advertised_prefixes
  - compute
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

Creates, updates, deletes or gets an <code>public_advertised_prefix</code> resource or lists <code>public_advertised_prefixes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_advertised_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.public_advertised_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="byoipApiVersion" /> | `string` | [Output Only] The version of BYOIP API. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="dnsVerificationIp" /> | `string` | The address to be used for reverse DNS verification. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicAdvertisedPrefix. An up-to-date fingerprint must be provided in order to update the PublicAdvertisedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicAdvertisedPrefix. |
| <CopyableCode code="ipCidrRange" /> | `string` | The address range, in CIDR format, represented by this public advertised prefix. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#publicAdvertisedPrefix for public advertised prefixes. |
| <CopyableCode code="pdpScope" /> | `string` | Specifies how child public delegated prefix will be scoped. It could be one of following values: - `REGIONAL`: The public delegated prefix is regional only. The provisioning will take a few minutes. - `GLOBAL`: The public delegated prefix is global only. The provisioning will take ~4 weeks. - `GLOBAL_AND_REGIONAL` [output only]: The public delegated prefixes is BYOIP V1 legacy prefix. This is output only value and no longer supported in BYOIP V2.  |
| <CopyableCode code="publicDelegatedPrefixs" /> | `array` | [Output Only] The list of public delegated prefixes that exist for this public advertised prefix. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="sharedSecret" /> | `string` | [Output Only] The shared secret to be used for reverse DNS verification. |
| <CopyableCode code="status" /> | `string` | The status of the public advertised prefix. Possible values include: - `INITIAL`: RPKI validation is complete. - `PTR_CONFIGURED`: User has configured the PTR. - `VALIDATED`: Reverse DNS lookup is successful. - `REVERSE_DNS_LOOKUP_FAILED`: Reverse DNS lookup failed. - `PREFIX_CONFIGURATION_IN_PROGRESS`: The prefix is being configured. - `PREFIX_CONFIGURATION_COMPLETE`: The prefix is fully configured. - `PREFIX_REMOVAL_IN_PROGRESS`: The prefix is being removed.  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, publicAdvertisedPrefix" /> | Returns the specified PublicAdvertisedPrefix resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists the PublicAdvertisedPrefixes for a project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, publicAdvertisedPrefix" /> | Deletes the specified PublicAdvertisedPrefix |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, publicAdvertisedPrefix" /> | Patches the specified Router resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| <CopyableCode code="announce" /> | `EXEC` | <CopyableCode code="project, publicAdvertisedPrefix" /> | Announces the specified PublicAdvertisedPrefix |
| <CopyableCode code="withdraw" /> | `EXEC` | <CopyableCode code="project, publicAdvertisedPrefix" /> | Withdraws the specified PublicAdvertisedPrefix |

## `SELECT` examples

Lists the PublicAdvertisedPrefixes for a project.

```sql
SELECT
id,
name,
description,
byoipApiVersion,
creationTimestamp,
dnsVerificationIp,
fingerprint,
ipCidrRange,
kind,
pdpScope,
publicDelegatedPrefixs,
selfLink,
sharedSecret,
status
FROM google.compute.public_advertised_prefixes
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_advertised_prefixes</code> resource.

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
INSERT INTO google.compute.public_advertised_prefixes (
project,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
ipCidrRange,
dnsVerificationIp,
sharedSecret,
status,
pdpScope,
publicDelegatedPrefixs,
fingerprint,
byoipApiVersion
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ ipCidrRange }}',
'{{ dnsVerificationIp }}',
'{{ sharedSecret }}',
'{{ status }}',
'{{ pdpScope }}',
'{{ publicDelegatedPrefixs }}',
'{{ fingerprint }}',
'{{ byoipApiVersion }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: ipCidrRange
        value: '{{ ipCidrRange }}'
      - name: dnsVerificationIp
        value: '{{ dnsVerificationIp }}'
      - name: sharedSecret
        value: '{{ sharedSecret }}'
      - name: status
        value: '{{ status }}'
      - name: pdpScope
        value: '{{ pdpScope }}'
      - name: publicDelegatedPrefixs
        value: '{{ publicDelegatedPrefixs }}'
      - name: fingerprint
        value: '{{ fingerprint }}'
      - name: byoipApiVersion
        value: '{{ byoipApiVersion }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a public_advertised_prefix only if the necessary resources are available.

```sql
UPDATE google.compute.public_advertised_prefixes
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
ipCidrRange = '{{ ipCidrRange }}',
dnsVerificationIp = '{{ dnsVerificationIp }}',
sharedSecret = '{{ sharedSecret }}',
status = '{{ status }}',
pdpScope = '{{ pdpScope }}',
publicDelegatedPrefixs = '{{ publicDelegatedPrefixs }}',
fingerprint = '{{ fingerprint }}',
byoipApiVersion = '{{ byoipApiVersion }}'
WHERE 
project = '{{ project }}'
AND publicAdvertisedPrefix = '{{ publicAdvertisedPrefix }}';
```

## `DELETE` example

Deletes the specified public_advertised_prefix resource.

```sql
DELETE FROM google.compute.public_advertised_prefixes
WHERE project = '{{ project }}'
AND publicAdvertisedPrefix = '{{ publicAdvertisedPrefix }}';
```
