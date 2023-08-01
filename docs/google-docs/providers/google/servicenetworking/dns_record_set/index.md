---
title: dns_record_set
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_record_set
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_record_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.dns_record_set</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `array` | Required. As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) for examples see https://cloud.google.com/dns/records/json-record. |
| `domain` | `string` | Required. The DNS or domain name of the record set, e.g. `test.example.com`. Cloud DNS requires that a DNS suffix ends with a trailing dot. |
| `ttl` | `string` | Required. The period of time for which this RecordSet can be cached by resolvers. |
| `type` | `string` | Required. The identifier of a supported record type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `servicesId` |
