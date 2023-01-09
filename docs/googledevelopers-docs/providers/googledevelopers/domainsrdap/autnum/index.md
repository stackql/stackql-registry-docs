---
title: autnum
hide_title: false
hide_table_of_contents: false
keywords:
  - autnum
  - domainsrdap
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autnum</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.domainsrdap.autnum</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `array` | Error description. |
| `notices` | `array` | Notices applying to this response. |
| `rdapConformance` | `array` | RDAP conformance level. |
| `title` | `string` | Error title. |
| `errorCode` | `integer` | Error HTTP code. Example: "501". |
| `jsonResponse` | `object` | Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest &#123; // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; &#125; service ResourceService &#123; rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); &#125; Example with streaming methods: service CaldavService &#123; rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); &#125; Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged. |
| `lang` | `string` | Error language code. Error response info fields are defined in [section 6 of RFC 7483](https://tools.ietf.org/html/rfc7483#section-6). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `autnumId` |
