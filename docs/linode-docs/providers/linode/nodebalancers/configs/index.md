---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - nodebalancers
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This config's unique ID |
| <CopyableCode code="algorithm" /> | `string` | What algorithm this NodeBalancer should use for routing traffic to backends.<br /> |
| <CopyableCode code="check" /> | `string` | The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down.<br />* If `none` no check is performed.<br />* `connection` requires only a connection to the backend to succeed.<br />* `http` and `http_body` rely on the backend serving HTTP, and that<br />  the response returned matches what is expected.<br /> |
| <CopyableCode code="check_attempts" /> | `integer` | How many times to attempt a check before considering a backend to be down.<br /> |
| <CopyableCode code="check_body" /> | `string` | This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down.<br /> |
| <CopyableCode code="check_interval" /> | `integer` | How often, in seconds, to check that backends are up and serving requests.<br /><br />Must be greater than `check_timeout`.<br /> |
| <CopyableCode code="check_passive" /> | `boolean` | If true, any response from this backend with a `5xx` status code will be enough for it to be considered unhealthy and taken out of rotation.<br /> |
| <CopyableCode code="check_path" /> | `string` | The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.<br /> |
| <CopyableCode code="check_timeout" /> | `integer` | How long, in seconds, to wait for a check attempt before considering it failed.<br /><br />Must be less than `check_interval`.<br /> |
| <CopyableCode code="cipher_suite" /> | `string` | What ciphers to use for SSL connections served by this NodeBalancer.<br /><br />* `legacy` is considered insecure and should only be used if necessary.<br /> |
| <CopyableCode code="nodebalancer_id" /> | `integer` | The ID for the NodeBalancer this config belongs to.<br /> |
| <CopyableCode code="nodes_status" /> | `object` | A structure containing information about the health of the backends for this port.  This information is updated periodically as checks are performed against backends.<br /> |
| <CopyableCode code="port" /> | `integer` | The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443.<br /> |
| <CopyableCode code="protocol" /> | `string` | The protocol this port is configured to serve.<br /><br />* The `http` and `tcp` protocols do not support `ssl_cert` and `ssl_key`.<br /><br />* The `https` protocol is mutually required with `ssl_cert` and `ssl_key`.<br /><br />Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features.<br /> |
| <CopyableCode code="proxy_protocol" /> | `string` | ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.<br /><br />* If ommited, or set to `none`, the NodeBalancer doesn't send any auxilary data over TCP connections. This is the default.<br />* If set to `v1`, the human-readable header format (Version 1) is used. Requires `tcp` protocol.<br />* If set to `v2`, the binary header format (Version 2) is used. Requires `tcp` protocol.<br /> |
| <CopyableCode code="ssl_cert" /> | `string` | The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL<br />certificate and Certificate Authority chain) that should be served on this<br />NodeBalancerConfig's port.<br /><br />Line breaks must be represented as "\n" in the string for requests (but not when using the Linode CLI).<br /><br />[Diffie-Hellman Parameters](/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.<br /><br />The contents of this field will not be shown in any responses that display<br />the NodeBalancerConfig. Instead, `&lt;REDACTED&gt;` will be printed where the field<br />appears.<br /><br />The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig<br />response are automatically derived from your certificate. Please refer to these fields to<br />verify that the appropriate certificate was assigned to your NodeBalancerConfig.<br /> |
| <CopyableCode code="ssl_commonname" /> | `string` | The read-only common name automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig.<br /> |
| <CopyableCode code="ssl_fingerprint" /> | `string` | The read-only SHA1-encoded fingerprint automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig.<br /> |
| <CopyableCode code="ssl_key" /> | `string` | The PEM-formatted private key for the SSL certificate set in the `ssl_cert` field.<br /><br />Line breaks must be represented as "\n" in the string for requests (but not when using the Linode CLI).<br /><br />The contents of this field will not be shown in any responses that display<br />the NodeBalancerConfig. Instead, `&lt;REDACTED&gt;` will be printed where the field<br />appears.<br /><br />The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig<br />response are automatically derived from your certificate. Please refer to these fields to<br />verify that the appropriate certificate was assigned to your NodeBalancerConfig.<br /> |
| <CopyableCode code="stickiness" /> | `string` | Controls how session stickiness is handled on this port.<br />* If set to `none` connections will always be assigned a backend based on the algorithm configured.<br />* If set to `table` sessions from the same remote address will be routed to the same<br />  backend.<br /><br />* For HTTP or HTTPS clients, `http_cookie` allows sessions to be<br />  routed to the same backend based on a cookie set by the NodeBalancer.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getNodeBalancerConfig" /> | `SELECT` | <CopyableCode code="configId, nodeBalancerId" /> | Returns configuration information for a single port of this NodeBalancer.<br /> |
| <CopyableCode code="getNodeBalancerConfigs" /> | `SELECT` | <CopyableCode code="nodeBalancerId" /> | Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.<br /><br />For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80.<br /> |
| <CopyableCode code="createNodeBalancerConfig" /> | `INSERT` | <CopyableCode code="nodeBalancerId" /> | Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests.<br /> |
| <CopyableCode code="deleteNodeBalancerConfig" /> | `DELETE` | <CopyableCode code="configId, nodeBalancerId" /> | Deletes the Config for a port of this NodeBalancer.<br /><br />**This cannot be undone.**<br /><br />Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed.<br /> |
| <CopyableCode code="_getNodeBalancerConfig" /> | `EXEC` | <CopyableCode code="configId, nodeBalancerId" /> | Returns configuration information for a single port of this NodeBalancer.<br /> |
| <CopyableCode code="_getNodeBalancerConfigs" /> | `EXEC` | <CopyableCode code="nodeBalancerId" /> | Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.<br /><br />For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80.<br /> |
| <CopyableCode code="rebuildNodeBalancerConfig" /> | `EXEC` | <CopyableCode code="configId, nodeBalancerId" /> | Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.<br /><br />Use this command to update a NodeBalancer's Config and Nodes with a single request.<br /> |
| <CopyableCode code="updateNodeBalancerConfig" /> | `EXEC` | <CopyableCode code="configId, nodeBalancerId" /> | Updates the configuration for a single port on a NodeBalancer.<br /> |
