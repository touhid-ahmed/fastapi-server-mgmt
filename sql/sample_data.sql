INSERT INTO public.datacenter (id, name, created_at) VALUES (1, 'germany-badenbaden', '2024-05-28 11:31:39.239320');
INSERT INTO public.datacenter (id, name, created_at) VALUES (2, 'germany-frankfurt', '2024-05-28 11:36:05.548255');
INSERT INTO public.datacenter (id, name, created_at) VALUES (3, 'uk-manchester', '2024-05-28 11:36:05.548255');


INSERT INTO public.switch (id, name, vlans, created_at, modified_at) VALUES (1, 'room 1', '{13,14,15}', '2024-05-28 11:37:39.782198', '2024-05-28 11:37:39.782198');
INSERT INTO public.switch (id, name, vlans, created_at, modified_at) VALUES (2, 'room 2', '{16,17}', '2024-05-28 11:38:15.486135', '2024-05-28 11:38:15.486135');
INSERT INTO public.switch (id, name, vlans, created_at, modified_at) VALUES (3, 'room 2b', '{1,14}', '2024-05-28 11:38:15.486135', '2024-05-28 11:38:15.486135');


INSERT INTO public.server (id, hostname, configuration, datacenter_id, created_at, modified_at) VALUES (1, 'myserver.local.lan', '{}', 1, '2024-05-28 11:39:01.516030', '2024-05-28 11:39:01.516030');
INSERT INTO public.server (id, hostname, configuration, datacenter_id, created_at, modified_at) VALUES (2, 'database.local.lan', '{"user_limit": 10, "max_connections": 500}', 2, '2024-05-28 11:40:13.349528', '2024-05-28 11:40:13.349528');
INSERT INTO public.server (id, hostname, configuration, datacenter_id, created_at, modified_at) VALUES (3, 'rabbitmq.local.lan', '{"max_queues": 1234}', 2, '2024-05-28 11:41:14.626643', '2024-05-28 11:41:14.626643');



INSERT INTO public.switch_to_server (switch_id, server_id) VALUES (1, 1);
INSERT INTO public.switch_to_server (switch_id, server_id) VALUES (1, 2);
INSERT INTO public.switch_to_server (switch_id, server_id) VALUES (1, 3);
INSERT INTO public.switch_to_server (switch_id, server_id) VALUES (2, 3);

SELECT pg_catalog.setval(pg_get_serial_sequence('public.server', 'id'), MAX(id)) FROM public.server;
SELECT pg_catalog.setval(pg_get_serial_sequence('public.datacenter', 'id'), MAX(id)) FROM public.datacenter;
SELECT pg_catalog.setval(pg_get_serial_sequence('public.switch', 'id'), MAX(id)) FROM public.switch;