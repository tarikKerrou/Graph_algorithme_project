import tkinter as tk
from graph import Graph

root = tk.Tk()
root.geometry("1440x840+300+300")  # width x height + x + y
# root.resizable(width=False, height=False)
root.title("GraphApp V 1.O")
first__page = tk.Frame(root)
second_page = tk.Frame(root)
main_frame = tk.Frame(root)  # Third Page
four_page = tk.Frame(root)
graph_info_frame = tk.Frame(root, pady=200, padx=200)
inputs = []
is_oriented_variable = tk.BooleanVar(second_page)
is_weighted_variable = tk.BooleanVar(second_page)
algorithm_input_variable = tk.StringVar(four_page)
kruskal_list = []


def display_graph():
    new_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    if is_oriented_variable.get():
        new_graph.display_digraph()
    else:
        new_graph.display_graph()


def show_graph_infos():
    # Show Graph Information
    new_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    new_graph.create_arcs()
    new_graph.create_nodes()
    new_graph.create_adjacency_list()
    new_graph.create_incidence_matrix()
    is_simple = new_graph.is_simple()
    is_complete = new_graph.is_complete()
    is_related = new_graph.is_related()
    is_euler = new_graph.is_eulerian()
    graph_info_frame.pack()
    infos_label = tk.Label(graph_info_frame,
                           text=f'Simple   : {is_simple} ||'
                                f'Complet  : {is_complete} ||'
                                f'Connex   : {is_related} ||'
                                f'Eulerian : {is_euler}', font='Arial 15')
    infos_label.pack()

    # Show Graph Information


def apply_algorithm():
    my_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    algorithm_name = algorithm_input_variable.get()
    kruskal_list = []

    def draw_result_kruskal():
        final_shape = Graph(inputs=kruskal_list, is_wheited=is_weighted_variable.get())
        final_shape.display_graph()

    def draw_result_prim():
        final_shape_prim = Graph(inputs=run_prime(), is_wheited=is_weighted_variable.get())
        final_shape_prim.display_graph()

    def draw_result_dijkstra():
        final_shape_dijkstra = Graph(inputs=run_dijkstra(), is_wheited=is_weighted_variable.get())
        final_shape_dijkstra.display_graph()

    if algorithm_name == 'Kruskal':
        graph_info_frame.destroy()
        kruskal_frame = tk.Frame(root)
        kruskal_frame.pack()
        kruskal_list = [(item[0] + item[2], item[1]) for item in my_graph.kruskal()]
        kruskal_header = tk.Label(kruskal_frame, text=f'La liste finale des arc : {kruskal_list}', font='Arial 15')
        kruskal_header.pack()
        kruskal_draw_button = tk.Button(kruskal_frame, text="Forme Graphique", command=draw_result_kruskal)
        kruskal_draw_button.pack()

    elif algorithm_name == 'Prime':

        def run_prime():
            prim_frame.destroy()
            prim2_frame = tk.Frame(root)
            prim2_frame.pack()
            prime_list = my_graph.prime(start_point.get())
            prim_header = tk.Label(prim2_frame, text=f'La liste finale des arc : {prime_list}', font='Arial 15')
            prim_header.pack()
            prim_draw_button = tk.Button(prim2_frame, text="Forme Graphique", command=draw_result_prim)
            prim_draw_button.pack()
            return prime_list

        graph_info_frame.destroy()
        prim_frame = tk.Frame(root)
        prim_frame.pack()
        prime_start_node_variable = tk.StringVar(prim_frame)
        prime_start_node_label = tk.Label(prim_frame, text="Le Point De Depart: ")
        prime_start_node_label.pack()
        prime_start_node_entry = tk.Entry(prim_frame, textvariable=prime_start_node_variable)
        prime_start_node_entry.pack()
        prime_start_node_button = tk.Button(prim_frame, text="Start", command=run_prime)
        prime_start_node_button.pack()
        start_point = prime_start_node_variable

    elif algorithm_name == 'Dijkstra':

        def run_dijkstra():
            dijkstra_frame.destroy()
            dijkstra2_frame = tk.Frame(root)
            dijkstra2_frame.pack()
            dijkstra_list = my_graph.dijkstra(start_point_dijkstra.get())
            dijkstra_header = tk.Label(dijkstra2_frame,
                                       text='Les Listes finales de votres Graphe : ',
                                       font='Arial 15')
            dijkstra_header.pack()
            dijkstra_table = tk.Label(dijkstra2_frame, text=f'{dijkstra_list}')
            dijkstra_table.pack()
            dijkstra_draw_button = tk.Button(dijkstra2_frame, text="Forme Graphique",
                                             font='Arial 10')  # command=draw_result_dijkstra
            dijkstra_draw_button.pack()

        graph_info_frame.destroy()
        dijkstra_frame = tk.Frame(root)
        dijkstra_frame.pack()
        dijkstra_start_node_variable = tk.StringVar(dijkstra_frame)
        dijkstra_start_node_label = tk.Label(dijkstra_frame, text="Le Point De Depart: ")
        dijkstra_start_node_label.pack()
        dijkstra_start_node_entry = tk.Entry(dijkstra_frame, textvariable=dijkstra_start_node_variable)
        dijkstra_start_node_entry.pack()
        dijkstra_start_node_button = tk.Button(dijkstra_frame, text="Start", command=run_dijkstra)
        dijkstra_start_node_button.pack()
        start_point_dijkstra = dijkstra_start_node_variable

    elif algorithm_name == 'Bellman-Ford':
        def run_bellmanf():
            bellmanf_frame.destroy()
            bellmanf2_frame = tk.Frame(root)
            bellmanf2_frame.pack()
            bellmanf_list = my_graph.bellman_ford(start_point_bellmanf.get())
            bellmanf_header = tk.Label(bellmanf2_frame,
                                       text=f'Les Listes finales de votres Graphe : ',
                                       font='Arial 15')
            bellmanf_header.pack()
            bellmanf_table = tk.Label(bellmanf2_frame, text=f'{bellmanf_list}')
            bellmanf_table.pack()
            bellmanf_draw_button = tk.Button(bellmanf2_frame, text="Forme Graphique", )  # command=draw_result_dijkstra
            bellmanf_draw_button.pack()
            return bellmanf_list

        graph_info_frame.destroy()
        bellmanf_frame = tk.Frame(root)
        bellmanf_frame.pack()
        bellmanf_start_node_variable = tk.StringVar(bellmanf_frame)
        bellmanf_start_node_label = tk.Label(bellmanf_frame, text="Le Point De Depart: ")
        bellmanf_start_node_label.pack()
        bellmanf_start_node_entry = tk.Entry(bellmanf_frame, textvariable=bellmanf_start_node_variable)
        bellmanf_start_node_entry.pack()
        bellmanf_start_node_button = tk.Button(bellmanf_frame, text="Start", command=run_bellmanf)
        bellmanf_start_node_button.pack()
        start_point_bellmanf = bellmanf_start_node_variable

    elif algorithm_name == 'DFS':
        pass

    elif algorithm_name == 'BFS':
        pass


def fourth_page():
    main_frame.destroy()
    four_page = tk.Frame(root)
    four_page.pack(pady=200)
    main_label = tk.Label(four_page, text="Votre Graphe est Crée", font="kefa 20")
    main_label.pack()
    display_graph_label = tk.Label(four_page, text="Appercue Votre Graphe")
    display_graph_label.pack()
    display_graph_button = tk.Button(four_page, text="Afficher", command=display_graph)
    display_graph_button.pack(padx=20, pady=10, ipady=5, ipadx=10)
    display_graph_info_label = tk.Label(four_page, text="Afficher les informations de votre graphe")
    display_graph_info_label.pack()
    display_graph_info_button = tk.Button(four_page, text="Afficher", command=show_graph_infos)
    display_graph_info_button.pack(padx=20, pady=10, ipady=5, ipadx=10)
    apply_algorithme_label = tk.Label(four_page, text="Appliquer Un Algorithm sur votre Graphe")
    apply_algorithme_label.pack(pady=10)
    values = ['Kruskal', 'Prime', 'Dijkstra', 'Bellman-Ford', 'BFS', 'DFS']
    algorithms_input = tk.OptionMenu(four_page, algorithm_input_variable, *values)
    algorithms_input.pack()
    algorithm_apply_button = tk.Button(four_page, text='Appliquer', command=apply_algorithm)
    algorithm_apply_button.pack(pady=20)


def graph_info_page():
    first__page.destroy()
    second_page.pack()
    second_page_header = tk.Label(second_page, text="Entrer Les Informations de votre Graphe", font="Arial 26")
    second_page_header.pack(pady=100)
    edges_variable = tk.IntVar(second_page)
    edge_label = tk.Label(second_page, text='Le nombres d\'arrêts de votre graphe ?')
    edge_label.pack()
    edges_entry = tk.Entry(second_page, textvariable=edges_variable)
    edges_entry.pack()
    edges_number_error = tk.Label(second_page, fg='red')
    edges_number_error.pack()

    is_weighted_label = tk.Label(second_page, text="est ce que vos arrêts ont des capacités ?")
    is_weighted_label.pack()
    is_weighted_input = tk.Checkbutton(second_page, variable=is_weighted_variable)
    is_weighted_input.pack(pady=5, ipady=5)
    is_oriented_label = tk.Label(second_page, text="est ce que votre graphe est orienté ?")
    is_oriented_label.pack()
    is_oriented_input = tk.Checkbutton(second_page, variable=is_oriented_variable)
    is_oriented_input.pack()

    # The Third Page Where User Should Enter The Graph's edges infos
    def graph_edges_info_page():
        second_page.destroy()
        main_frame.pack(expand=1, fill="both")
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side="left", fill="both", expand=1)

        scroll_bar = tk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
        scroll_bar.pack(side="right", fill="y")

        my_canvas.configure(yscrollcommand=scroll_bar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)
        my_canvas.create_window((600, 50), window=second_frame, anchor="nw")
        third_page_header = tk.Label(second_frame, text="Entrer Les Informations de vos arret", font="kefa 20")
        third_page_header.grid(row=0, columnspan=3)
        widgets_inputs_list = []

        # Get and Store The User Inputs

        def append_inputs():
            for item in widgets_inputs_list:
                if is_weighted_variable.get():
                    inputs.append((item[0].get(), item[1].get()))
                else:
                    inputs.append(item.get())

            fourth_page()

        # Get and Store The User Inputs End

        # Generate The List Of Entries For User Inputs(graph Information)

        edges_number = edges_variable.get()

        if is_weighted_variable.get():
            for i in range(edges_number):
                # edge_weight_variable = tk.IntVar(second_frame)
                edge_name_label = tk.Label(second_frame, text=f'Arc {i + 1}')
                edge_weight_label = tk.Label(second_frame, text=f'Capacité {i + 1}')
                edge_name_label.grid(row=i + 1, column=i - i)
                edge_weight_label.grid(row=i + 1, column=i + 2 - i)
                edge_name_entry = tk.Entry(second_frame, )
                edge_weight_entry = tk.Entry(second_frame, )
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                edge_weight_entry.grid(row=i + 1, column=i + 3 - (i - 1))
                edges_weight_error = tk.Label(second_frame, fg='red')
                edges_weight_error.grid(row=i + 2, column=i + 3 - (i - 1))
                widgets_inputs_list.append((edge_name_entry, edge_weight_entry))

                # Error Handling
                def only_integer(data):
                    if data.isdigit():
                        return True
                    else:
                        return False

                def only_integers_errors(data):
                    edges_weight_error.configure(
                        text=f'Entrer Un Entier Posistive'
                    )

                register_only_ints = second_page.register(only_integer)
                register_only_errors = second_page.register(only_integers_errors)
                edge_weight_entry.config(validate='all',
                                         validatecommand=(register_only_ints, '%P'),
                                         invalidcommand=(register_only_errors, '%P'))
                # Error Handling End
        else:
            for i in range(edges_number):
                edge_name_label = tk.Label(second_frame, text=f'Arc {i}')
                edge_name_label.grid(row=i + 1, column=i - i)
                edge_name_entry = tk.Entry(second_frame, )
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                widgets_inputs_list.append(edge_name_entry)

        # Generate The List Of Entries For User Inputs(graph's Information) End

        # Submit Button for inputs
        show_inputs_button = tk.Button(second_frame, text="Creer", command=append_inputs)
        show_inputs_button.grid(columnspan=2)
        label = tk.Label(second_frame, )
        label.grid()

        # Submit Button End

    # Start Error Handling for Edges Entry IN second_page

    def only_integers(data):
        if data.isdigit():
            return True
        else:
            return False

    def only_integers_error(data):
        edges_number_error.configure(
            text=f'Entrer Un Entier Posistive'
        )

    register_only_int = second_page.register(only_integers)
    register_only_error = second_page.register(only_integers_error)
    edges_entry.config(validate='all',
                       validatecommand=(register_only_int, '%P'),
                       invalidcommand=(register_only_error, '%P'))

    # End of Error Handling

    # Submit Button for Second page

    submit_button = tk.Button(second_page, text='Entrer', command=graph_edges_info_page)
    submit_button.pack(padx=20, pady=10, ipady=5, ipadx=10)

    # Submit Button End


def first_page():
    first__page.pack(expand=1, fill="both", pady=150)
    first_page_header = tk.Label(first__page, text="Bienvenue dans GraphApp", font='Kefa 32 ', fg='#000')
    first_page_sub_header = tk.Label(first__page, text="Explorer Vos Graphes", font='Kefa 20 ', fg='#000')
    first_page_header.pack()
    first_page_sub_header.pack()
    create_button = tk.Button(first__page, text=" + Creer ", bg='blue', command=graph_info_page)
    create_button.pack(padx=20, pady=200, ipady=5, ipadx=10)


first_page()

root.mainloop()
