---
title: dns_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_keys
  - dns
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
<tr><td><b>Name</b></td><td><code>dns_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.dns_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the resource; defined by the server (output only). |
| `description` | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the resource's function. |
| `digests` | `array` | Cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Output only. |
| `keyTag` | `integer` | The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B. Output only. |
| `publicKey` | `string` | Base64 encoded public half of this key. Output only. |
| `type` | `string` | One of "KEY_SIGNING" or "ZONE_SIGNING". Keys of type KEY_SIGNING have the Secure Entry Point flag set and, when active, are used to sign only resource record sets of type DNSKEY. Otherwise, the Secure Entry Point flag is cleared, and this key is used to sign only resource record sets of other types. Immutable after creation time. |
| `kind` | `string` |  |
| `creationTime` | `string` | The time that this resource was created in the control plane. This is in RFC3339 text format. Output only. |
| `isActive` | `boolean` | Active keys are used to sign subsequent changes to the ManagedZone. Inactive keys are still present as DNSKEY Resource Records for the use of resolvers validating existing signatures. |
| `algorithm` | `string` | String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. |
| `keyLength` | `integer` | Length of the key in bits. Specified at creation time, and then immutable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `dnsKeys_get` | `SELECT` | `dnsKeyId, managedZone, project` | Fetches the representation of an existing DnsKey. |
| `dnsKeys_list` | `SELECT` | `managedZone, project` | Enumerates DnsKeys to a ResourceRecordSet collection. |
